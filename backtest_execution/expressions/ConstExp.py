import pandas as pd

from backtest_execution.expressions.Expression import Expression


class ConstExp(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def evaluate(self, index, df: pd.DataFrame):
        return self.value

    def __repr__(self):
        return str(self.value)
