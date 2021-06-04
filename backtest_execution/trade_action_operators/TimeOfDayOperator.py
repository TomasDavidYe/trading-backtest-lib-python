from backtest_execution.trade_action_operators.TradeActionOperator import TradeActionOperator
from backtest_execution.trade_actions.TradeAction import TradeAction
from enums.TimeOfDay import TimeOfDay


class TimeOfDayOperator(TradeActionOperator):
    def __init__(self, time_of_day: TimeOfDay):
        super().__init__()
        self.time_of_day = time_of_day

    def operate(self, action: TradeAction) -> TradeAction:
        if action.time_of_day is not None and action.time_of_day != self.time_of_day:
            raise Exception(f'Cannot set field "time_of_day" to "{self.time_of_day.value}" for TRADE_ACTION = {action} because it is already set to "{self.time_of_day.value}"')
        else:
            action.time_of_day = self.time_of_day
            return action
