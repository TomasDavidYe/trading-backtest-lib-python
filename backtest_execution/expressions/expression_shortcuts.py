from backtest_execution.expressions.CandleExp import CandleExp
from backtest_execution.expressions.ConstExp import ConstExp
from backtest_execution.expressions.Expression import Expression
from backtest_execution.expressions.SymbolExp import SymbolExp
from utils.constants.candle_constants import CLOSE, OPEN, HIGH, VOLUME


def sma(shift, k, column=CLOSE):
    result = CandleExp(column=column, shift=shift)
    for i in range(1, k):
        result = result + CandleExp(column=column, shift=shift-i)

    result.__repr__ = lambda: f'sma(n + ({shift}) ,{k})'
    return result / const(k)




def sym() -> Expression:
    return SymbolExp()


def o_n(shift) -> Expression:
    return CandleExp(shift=shift, column=OPEN)


def h_n(shift) -> Expression:
    return CandleExp(shift=shift, column=HIGH)


def l_n(shift) -> Expression:
    return CandleExp(shift=shift, column=HIGH)


def c_n(shift) -> Expression:
    return CandleExp(shift=shift, column=CLOSE)


def v_n(shift) -> Expression:
    return CandleExp(shift=shift, column=VOLUME)


def const(value) -> Expression:
    return ConstExp(value=value)
