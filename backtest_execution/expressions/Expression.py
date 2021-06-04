import pandas as pd


class Expression:
    def __init__(self):
        pass

    def evaluate(self, index, df: pd.DataFrame):
        pass

    def __add__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) + other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} + {other.__repr__()} )'
        return result

    def __sub__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) - other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} - {other.__repr__()} )'
        return result

    def __mul__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) * other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} * {other.__repr__()} )'
        return result

    def __pow__(self, power):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) ** power
        result.__repr__ = lambda: f'{self.__repr__()}^{power} )'
        return result


    def __truediv__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) / other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} / {other.__repr__()} )'
        return result

    def __lt__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) < other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} < {other.__repr__()} )'
        return result


    def __le__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) <= other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} <= {other.__repr__()} )'
        return result


    def __eq__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) == other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} == {other.__repr__()} )'
        return result


    def __contains__(self, key):
        result = Expression()
        result.evaluate = lambda index, df: key.evaluate(index, df) in self.evaluate(index, df)
        result.__repr__ = lambda: f'( {key.__repr__()} in {self.__repr__()} )'
        return result


    def __ne__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) != other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} != {other.__repr__()} )'
        return result


    def __gt__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) > other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} > {other.__repr__()} )'
        return result


    def __ge__(self, other):
        result = Expression()
        result.evaluate = lambda index, df: self.evaluate(index, df) >= other.evaluate(index, df)
        result.__repr__ = lambda: f'( {self.__repr__()} >= {other.__repr__()} )'
        return result





