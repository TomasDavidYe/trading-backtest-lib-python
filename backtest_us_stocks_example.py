from algorithms.RuleBasedAlgorithm import RuleBasedAlgorithm
from backtest_execution.TradeActionInstruction import TradeActionInstruction
from backtest_execution.expressions.expression_shortcuts import sma, const
from backtest_execution.trade_action_operators.trade_action_shortcuts import close_position, on_market_open, \
    open_position, buy
from services.DatasetProviderService import DatasetProviderService
from services.TradeExecutionService import TradeExecutionService
from utils.log_utils import PrintLogger

logger = PrintLogger()

indices, candle_dict = DatasetProviderService(
    logger=logger
).get_candles_for_backtest(
    file_path='./data/yahoo_data_us.csv',
    start_date='2020-01-01',
    end_date='2020-03-01',
    date_shift=15
)



# Instructions are evaluated in a descending priority order with 1 action per symbol each candle
instructions = [
    close_position(on_market_open(TradeActionInstruction(rules=[
        (sma(-1, 5) - sma(-1, 15)) <= const(0)
    ]))),

    open_position(on_market_open(buy(rules=[
        (sma(-1, 5) - sma(-1, 15)) / sma(-1, 15) >= const(0.05)
    ])))
]

algorithm = RuleBasedAlgorithm(
    instructions=instructions,
    logger=logger
)

trade_executor = TradeExecutionService(
    candle_dict=candle_dict,
    indices=indices,
    max_open_positions=5,
    commission=0.001,
    starting_capital=5000,
    logger=logger
)

while trade_executor.has_next_step():
    trade_executor.next_step(algorithm=algorithm)

trade_executor.describe_results()
