from backtest_execution.trade_actions.TradeAction import TradeAction
from services.TradeExecutionService import TradeExecutionService


class ClosePositionAction(TradeAction):
    def __init__(self, index: tuple, symbol: str):
        super().__init__(index, symbol)
        self.index = index
        self.symbol = symbol

    def apply_itself_to(self, trade_executor: TradeExecutionService):
        if trade_executor.is_position_open(symbol=self.symbol):
            trade_executor.close_position(
                symbol=self.symbol,
                time_of_day=self.time_of_day
            )



