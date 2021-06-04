from backtest_execution.trade_action_operators.TradeActionOperator import TradeActionOperator
from backtest_execution.trade_actions.ClosePositionAction import ClosePositionAction
from backtest_execution.trade_actions.TradeAction import TradeAction


class ClosePositionOperator(TradeActionOperator):
    def __init__(self):
        super().__init__()

    def operate(self, action: TradeAction) -> TradeAction:
        if not isinstance(action, TradeAction):
            raise Exception(f'MarketOrderOperator can only be applied to plain TradeAction but supplied action is of TYPE = {type(action)}')
        elif action.time_of_day is None:
            raise Exception(f'Time of Day need to be specified for ACTION = {action}')
        else:
            return ClosePositionAction(
                index=action.index,
                symbol=action.symbol
            )
