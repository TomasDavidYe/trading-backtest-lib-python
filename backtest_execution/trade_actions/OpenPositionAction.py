from backtest_execution.trade_actions.TradeAction import TradeAction
from services.TradeExecutionService import TradeExecutionService


class OpenPositionAction(TradeAction):
    def __init__(self, index: tuple, symbol: str, market_order_action):
        super().__init__(index, symbol)
        self.index = index
        self.symbol = symbol
        self.market_order_action = market_order_action

    def apply_itself_to(self, trade_executor: TradeExecutionService):
        if not trade_executor.is_position_open(symbol=self.symbol):
            self.market_order_action.apply_itself_to(trade_executor)



