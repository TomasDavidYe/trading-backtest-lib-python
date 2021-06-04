from backtest_execution.TradeActionInstruction import TradeActionInstruction
from backtest_execution.trade_action_operators.ClosePositionOperator import ClosePositionOperator
from backtest_execution.trade_action_operators.MarketOrderOperator import MarketOrderOperator
from backtest_execution.trade_action_operators.OpenPositionOperator import OpenPositionOperator
from backtest_execution.trade_action_operators.TimeOfDayOperator import TimeOfDayOperator
from enums.OrderSide import OrderSide
from enums.TimeOfDay import TimeOfDay


def on_market_open(instruction: TradeActionInstruction) -> TradeActionInstruction:
    return TimeOfDayOperator(TimeOfDay.MARKET_OPEN)(instruction)


def on_market_close(instruction: TradeActionInstruction) -> TradeActionInstruction:
    return TimeOfDayOperator(TimeOfDay.MARKET_CLOSE)(instruction)


def buy(rules) -> TradeActionInstruction:
    return MarketOrderOperator(order_side=OrderSide.BUY)(TradeActionInstruction(rules=rules))


def sell(rules) -> TradeActionInstruction:
    return MarketOrderOperator(order_side=OrderSide.SELL)(TradeActionInstruction(rules=rules))


def open_position(instruction: TradeActionInstruction) -> TradeActionInstruction:
    return OpenPositionOperator()(instruction)


def close_position(instruction: TradeActionInstruction) -> TradeActionInstruction:
    return ClosePositionOperator()(instruction)
