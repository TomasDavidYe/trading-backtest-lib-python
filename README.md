## Description
Are you developing algo trading strategies via Python? Are you eager to back test your strategies on past datasets?
If so, then this package can help you.

I myself have spent significant amount of time developing trading backtesting frameworks and am eager to share the code with you to help you get started.

With the framework comes a set of utility functions which enables users to express simple trading strategies in a few lines of code and back test them on past data. 

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
The code below defines and algorithm which buys a stock (opens a position), when 5 day Simple Moving Average (SMA) is 1% higher than the 15 day SMA and sells it (closes the position) when the 5 day SMA goes back below 15 day SMA 


```python

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

Instructions are evaluated in a descending priority order with 1 action per symbol each candle.

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

## Create Your Own Algorithms
In case you want to design other algorithms via the framework, feel free to look at the [**expression_shortcuts**](./backtest_execution/expressions/expression_shortcuts.py) to see what expressions are currently implemented and you can combine them however you want to create a new trading strategy. 

If you want to create a new expression, you will need to create a new implementation of the [**Expression**](./backtest_execution/expressions/Expression.py). The key here is to implement the **.evaluate(index, df)** method which encodes how a value at a given index in the candle time series is evaluated. To get inspired, please have a look at how the simple expressions (found in [**expression_shortcuts**](./backtest_execution/expressions/expression_shortcuts.py)) are implemented. 

A nice feature of expressions is that they can be combined via arithmetic operations. This way, you can build very complex expressions from a few simple building blocks. To see this, take a look at how the Simple Moving Average indicator (SMA) is implemented in [**expression_shortcuts**](./backtest_execution/expressions/expression_shortcuts.py). 
 

## Contribute
This library is still very basic and miles away from a full-fledged back-testing framework for trading algorithms. Here are several ways I can see this to grow:
1. Implement more indicators by overriding the [**Expression**](./backtest_execution/expressions/Expression.py) class. For example, EMA or Boilinger bands are great candidates
1. Optimisation of the [**TradeExecutionService**](./services/TradeExecutionService.py). Currently, the back-tests take a while when running over a long period.

If you would like to contribute in any of the above (or some other way), ping me and let's discuss it :) I am super happy for any joint cooperation!