import pandas as pd

from backtest_execution.expressions.Expression import Expression
from utils.constants.candle_constants import SYMBOL


class SymbolExp(Expression):
    def __init__(self):
        super().__init__()

    def evaluate(self, index, df: pd.DataFrame):
        return df.loc[index][SYMBOL]

    def __repr__(self):
        return 'symbol'
