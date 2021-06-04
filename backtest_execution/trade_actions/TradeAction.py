from enums.TimeOfDay import TimeOfDay


class TradeAction:
    def __init__(self, index: tuple, symbol: str, time_of_day: TimeOfDay = None):
        self.time_of_day = time_of_day
        self.index = index
        self.symbol = symbol

    def apply_itself_to(self, trade_executor):
        raise NotImplementedError('This Method is Abstract')



