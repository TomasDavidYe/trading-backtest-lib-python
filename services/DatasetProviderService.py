import pandas as pd

from utils.constants.candle_constants import SYMBOL, DATE
from utils.string_utils import date_to_string, string_to_date


class DatasetProviderService:

    def __init__(self, logger):
        self.logger = logger

    def get_candles_for_backtest(self, file_path: str, start_date: str, end_date: str, date_shift: int = 0):
        candle_df: pd.DataFrame = pd.read_csv(file_path)
        candle_df = candle_df[(start_date <= candle_df[DATE]) & (candle_df[DATE] <= end_date)]
        symbols = set(candle_df[SYMBOL].unique())
        dates = list(candle_df[DATE].unique())

        dates.sort()

        candle_dict = {}

        for i, symbol in enumerate(symbols):
            self.logger.info(f'Loading dateset {i + 1}/{len(symbols)} (SYMBOL = {symbol})')
            candle_dict[symbol] = candle_df[candle_df[SYMBOL] == symbol].copy().sort_values(by=DATE).reset_index(drop=True)

        indices = [
            (i, string_to_date(dates[i], time_format='%Y-%m-%d'))  for i in range(date_shift, len(dates))
        ]

        return indices, candle_dict
