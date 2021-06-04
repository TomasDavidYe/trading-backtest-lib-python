from backtest_execution.trade_actions.TradeAction import TradeAction
from enums.TimeOfDay import TimeOfDay
from services.TradeExecutionService import TradeExecutionService


class MarketOrderAction(TradeAction):
    def __init__(self, index: tuple, symbol: str, order_side, time_of_day: TimeOfDay, quantity: float = None):
        super().__init__(index, symbol)
        self.time_of_day = time_of_day
        self.quantity = quantity
        self.index = index
        self.symbol = symbol
        self.order_side = order_side

    def apply_itself_to(self, trade_executor: TradeExecutionService):
        trade_executor.market_order(
            symbol=self.symbol,
            side=self.order_side,
            quantity=self.quantity,
            time_of_day=self.time_of_day
        )



