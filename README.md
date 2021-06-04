## Description
Are you developing algo trading strategies via Python? Are you eager to back test your strategies on past datasets?
If so, then this package can help you.

I myself have spent significant amount of time developing trading backtesting frameworks and am eager to share the code with you to help you get started.

Below are instructions how to install and run the package. Reach out to me if you have problems running it or you would like to contribute :)

## How to install
```bash
git clone https://github.com/TomasDavidYe/trading-backtest-lib-python.git;
pip3 install -r requirements.txt
```
 

## Initialize a dataset
```python
indices, candle_dict = DatasetProviderService(
    logger=logger
).get_candles_for_backtest(
    file_path='./data/yahoo_data_us.csv',
    start_date='2020-01-01',
    end_date='2020-06-01',
    date_shift=15
)
```

## Initialize algorithm
```python
# Instructions are evaluated in a descending priority order with 1 action per symbol each candle
instructions = [
    close_position(on_market_open(TradeActionInstruction(rules=[
        (sma(-1, 5) - sma(-1, 15)) <= const(0)
    ]))),

    open_position(on_market_open(buy(rules=[
        (sma(-1, 5) - sma(-1, 15)) / sma(-1, 15) >= const(0.01)
    ])))
]

algorithm = RuleBasedAlgorithm(
    instructions=instructions,
    logger=logger
)
```

## Run Backtest with Algorithm on dataset
```python
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
```

## Full Example
[Backtest on US Stocks](./backtest_us_stocks_example.py)
```bash
pyton3 backtest_us_stocks_example.py
```

![](https://i.imgur.com/YTQKRYB.png)