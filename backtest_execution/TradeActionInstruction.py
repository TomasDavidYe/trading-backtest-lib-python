import pandas as pd

from backtest_execution.expressions.Expression import Expression
from backtest_execution.trade_actions.TradeAction import TradeAction
from utils.log_utils import PrintLogger
from utils.string_utils import date_to_string


class TradeActionInstruction:
    def __init__(self, rules, logger=PrintLogger()):
        self.rules = rules
        self.logger = logger
        self.transforms = []

    def register_transform(self, transform):
        self.transforms.append(transform)

    def transform(self, trade_action) -> TradeAction:
        result = trade_action
        for transform in self.transforms:
            result = transform(result)

        return result

    def evaluate(self, index: tuple, df: pd.DataFrame, symbol: str) -> bool:
        number_index = index[0]
        date = date_to_string(index[1])

        rule: Expression
        self.logger.debug(f'\n\n\n START Evaluation for TICKER = {symbol} on DATE = {date}')
        for i, rule in enumerate(self.rules):
            self.logger.debug(f'Rule evaluation {i + 1}/{len(self.rules)}')
            if rule.evaluate(df=df, index=number_index):
                self.logger.debug(f'Evaluation passed for RULE = {rule.__repr__()}')
            else:
                self.logger.debug(
                    f'END -> Evaluation failed and TICKER = {symbol} for DATE = {date} on RULE = {rule.__repr__()}')
                return False

            self.logger.debug(f'Evaluation passed for all {len(self.rules)} rules.')
            self.logger.debug(f'END -> Evaluation succeeded for TICKER = {symbol} for DATE = {date}')

        return True

    def decide_actions(self, index: tuple, candle_dict: dict) -> list:
        trading_actions = []

        for index_symbol, item in enumerate(candle_dict.items()):
            symbol: str = item[0]
            df: pd.DataFrame = item[1]
            self.logger.debug(f'Decision {index_symbol + 1}/{len(candle_dict)} for SYMBOL = "{symbol}"')

            if self.evaluate(index=index, df=df, symbol=symbol):
                self.logger.debug(f'Evaluation passed for SYMBOL = {symbol} -> adding to a trading action')
                new_trade_action = self.transform(TradeAction(index=index, symbol=symbol))
                trading_actions.append(new_trade_action)
            else:
                self.logger.debug(f'Evaluation failed for SYMBOL = {symbol} -> not adding to a trading action')

        return trading_actions
