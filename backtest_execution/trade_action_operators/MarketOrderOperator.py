from backtest_execution.trade_action_operators.TradeActionOperator import TradeActionOperator
from backtest_execution.trade_actions.MarketOrderAction import MarketOrderAction
from backtest_execution.trade_actions.TradeAction import TradeAction


class MarketOrderOperator(TradeActionOperator):
    def __init__(self, order_side, quantity=None):
        super().__init__()
        self.order_side = order_side
        self.quantity = quantity

    def operate(self, action: TradeAction) -> TradeAction:
        if not isinstance(action, TradeAction):
            raise Exception(f'MarketOrderOperator can only be applied to plain TradeAction but supplied action is of TYPE = {type(action)}')
        else:
            return MarketOrderAction(
                index=action.index,
                symbol=action.symbol,
                order_side=self.order_side,
                quantity=self.quantity,
                time_of_day=action.time_of_day
            )
