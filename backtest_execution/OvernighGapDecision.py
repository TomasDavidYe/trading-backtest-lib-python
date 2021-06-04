from trading_engine_source.utils.string_utils import to_json, date_to_string


class OvernightGapDecision:
    def __init__(self, date_of_open, date_of_close, stock_dict: dict):
        self.stock_dict = stock_dict
        self.date_of_open = date_of_open
        self.date_of_close = date_of_close

    def get_symbols(self) -> list:
        return list(self.stock_dict.keys())

    def get_stock_count_for_symbol(self, symbol: str) -> float:
        return self.stock_dict[symbol]

    def get_stock_dict(self) -> dict:
        return self.stock_dict

    def __repr__(self):
        return to_json({
            'date_of_open': date_to_string(self.date_of_open),
            'date_of_close': date_to_string(self.date_of_close),
            'orders': self.stock_dict
        })

