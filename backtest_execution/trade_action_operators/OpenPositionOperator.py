from backtest_execution.trade_action_operators.TradeActionOperator import TradeActionOperator
from backtest_execution.trade_actions.MarketOrderAction import MarketOrderAction
from backtest_execution.trade_actions.OpenPositionAction import OpenPositionAction
from backtest_execution.trade_actions.TradeAction import TradeAction


class OpenPositionOperator(TradeActionOperator):
    def __init__(self):
        super().__init__()

    def operate(self, action: TradeAction) -> TradeAction:
        if not isinstance(action, MarketOrderAction):
            raise Exception(f'MarketOrderOperator can only be applied to MarketOrderAction but supplied action is of TYPE = {type(action)}')
        elif action.time_of_day is None:
            raise Exception(f'Time of Day need to be specified for ACTION = {action}')
        else:
            return OpenPositionAction(
                index=action.index,
                symbol=action.symbol,
                market_order_action=action
            )
