import pandas as pd
from matplotlib import pyplot as plt

from algorithms.RuleBasedAlgorithm import RuleBasedAlgorithm
from backtest_execution.Position import Position
from backtest_execution.trade_actions.TradeAction import TradeAction
from enums.OrderSide import OrderSide
from enums.PositionType import PositionType
from enums.TimeOfDay import TimeOfDay
from utils.constants.candle_constants import ACTIONS, POSITIONS, CAPITAL_BEFORE, CAPITAL_AFTER, PROFIT, COMMISSION, \
    DATE, OPEN, CLOSE


class TradeExecutionService:

    @staticmethod
    def position_type_for_order_side(order_side: OrderSide):
        return PositionType.LONG if order_side == OrderSide.BUY else PositionType.SHORT

    def __init__(self, starting_capital: float, max_open_positions: int, commission: float, candle_dict: dict, indices: dict, logger):
        self.step_commission = 0
        self.step_profit = 0
        self.commission = commission
        self.current_capital = starting_capital
        self.starting_capital = starting_capital
        self.max_open_positions = max_open_positions
        self.current_capital = starting_capital
        self.logger = logger
        self.indices: dict = indices
        self.candle_dict = candle_dict
        self.current_index = 0
        self.open_positions = {}
        self.snapshots = {
            date: {
                ACTIONS: {},
                POSITIONS: {},
                CAPITAL_BEFORE: None,
                CAPITAL_AFTER: None,
                PROFIT: None,
                COMMISSION: None
            } for index, date in self.indices
        }

    def is_position_open(self, symbol) -> bool:
        return symbol in self.open_positions

    def close_position(self, symbol: str, time_of_day: TimeOfDay):
        if not self.is_position_open(symbol=symbol):
            raise Exception(f'Cannot close position for SYMBOL = {symbol} because there is no open position for it.')
        else:
            position: Position = self.open_positions[symbol]
            position_open_price = position.open_price
            position_close_price = self.get_current_price_for_symbol(symbol=symbol, time_of_day=time_of_day)
            trade_capital = position.quantity

            self.apply_commission(trade_capital=trade_capital)
            self.apply_profit(
                open_price=position_open_price,
                close_price=position_close_price,
                trade_capital=trade_capital
            )

            del self.open_positions[symbol]

    def apply_profit(self, open_price, close_price, trade_capital):
        profit_rel = (close_price - open_price) / trade_capital
        capital_after = (1 + profit_rel) * trade_capital
        profit = capital_after - trade_capital
        self.step_profit += profit

    def process_updates(self):
        pass

    def describe_results(self):
        profit_df = pd.DataFrame([
            {
                DATE: date,
                CAPITAL_BEFORE: self.snapshots[date][CAPITAL_BEFORE],
                PROFIT: self.snapshots[date][PROFIT],
                COMMISSION: self.snapshots[date][COMMISSION],
                CAPITAL_AFTER: self.snapshots[date][CAPITAL_AFTER]
            } for index, date in self.indices
        ])

        plt.plot(profit_df[DATE],
                 profit_df[CAPITAL_AFTER],
                 color="cornflowerblue",
                 label="y_pred",
                 linewidth=2)
        plt.title(
            f'Performance between {self.indices[0][1]} and {self.indices[-1][1]} starting from {self.starting_capital}$')
        plt.xlabel(f'time')
        plt.ylabel('capital in $')
        plt.legend(loc='upper left')
        plt.show()

    def has_next_step(self) -> bool:
        return self.current_index < len(self.indices)

    def increment_index(self) -> tuple:
        if self.has_next_step():
            new_number_index = self.current_index[0] + 1
            return new_number_index, self.indices[new_number_index]
        else:
            raise Exception('Trade Executor has iterated through all possible steps')

    def next_step(self, algorithm: RuleBasedAlgorithm):
        self.process_updates()
        index = self.indices[self.current_index]
        trade_actions: list = algorithm.decide(index, self.candle_dict)

        action: TradeAction
        for trade_action in trade_actions:
            trade_action.apply_itself_to(self)

        self.recalculate_capital()
        self.log_actions(actions=trade_actions)
        self.log_open_positions()

        self.current_index += 1

    def recalculate_capital(self):
        old_capital = self.current_capital
        new_capital = old_capital + self.step_profit - self.step_commission
        self.current_capital = new_capital

        current_date = self.get_current_date()
        self.snapshots[current_date][CAPITAL_BEFORE] = old_capital
        self.snapshots[current_date][CAPITAL_AFTER] = new_capital
        self.snapshots[current_date][PROFIT] = self.step_profit
        self.snapshots[current_date][COMMISSION] = self.step_commission

        self.step_profit = 0
        self.step_commission = 0

    def log_actions(self, actions: list):
        date = self.get_current_date()

        action: TradeAction
        for action in actions:
            self.snapshots[date][ACTIONS][action.symbol] = action

    def log_open_positions(self):
        date = self.get_current_date()

        position: Position
        for symbol, position in self.open_positions.items():
            self.snapshots[date][POSITIONS][symbol] = position

    def get_current_date(self):
        return self.indices[self.current_index][1]

    def get_current_row_index(self):
        return self.indices[self.current_index][0]

    def apply_commission(self, trade_capital):
        trade_commission = trade_capital * self.commission
        self.step_commission += trade_commission

    def open_position(self, symbol: str, order_side: OrderSide, time_of_day: TimeOfDay, quantity: float = None):
        self.open_positions[symbol] = Position(
            symbol=symbol,
            position_type=self.position_type_for_order_side(order_side),
            open_price=self.get_current_price_for_symbol(symbol=symbol, time_of_day=time_of_day),
            quantity=quantity
        )

    def get_current_price_for_symbol(self, symbol: str, time_of_day: TimeOfDay):
        price_column = OPEN if time_of_day == TimeOfDay.MARKET_OPEN else CLOSE
        row_index = self.get_current_row_index()
        return self.candle_dict[symbol][price_column][row_index]

    def market_order(self, symbol: str, side: OrderSide, time_of_day: TimeOfDay, quantity=None):
        if self.is_position_open(symbol):
            raise Exception(f'Cannot create market order for SYMBOL = "{symbol}" at INDEX = "{self.current_index}" because position is already open for this symbol...')
        elif len(self.open_positions) == self.max_open_positions:
            self.logger.info(f'Cannot create market order for SYMBOL = "{symbol}" at INDEX = "{self.current_index}" because the number of open positions is already at its maximum.')
        else:
            trade_capital = self.current_capital / self.max_open_positions
            self.apply_commission(trade_capital=trade_capital)
            self.open_position(
                symbol=symbol,
                order_side=side,
                time_of_day=time_of_day,
                quantity=trade_capital
            )
