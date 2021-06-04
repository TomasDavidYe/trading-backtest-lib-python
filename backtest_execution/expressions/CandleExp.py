import pandas as pd

from backtest_execution.expressions.Expression import Expression


class CandleExp(Expression):
    def __init__(self, column, shift=0):
        super().__init__()
        self.shift = shift
        self.column = column

    def evaluate(self, index, df: pd.DataFrame):
        try:
            return df.loc[index + self.shift][self.column]
        except KeyError as e:
            raise Exception(f'Key Error for INDEX = {index}, COLUMN = {self.column}, SHIFT = {self.shift},   ORIGINAL ERROR -> {e}')

    def __repr__(self):
        if self.shift == 0:
            return f'{self.column}(n)'
        elif self.shift > 0:
            return f'{self.column}(n + {self.shift})'
        else:
            return f'{self.column}(n - {-self.shift})'
