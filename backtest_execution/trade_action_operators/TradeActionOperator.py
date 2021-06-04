# TODO -> Add callable syntax https://treyhunner.com/2019/04/is-it-a-class-or-a-function-its-a-callable/
from backtest_execution.TradeActionInstruction import TradeActionInstruction
from backtest_execution.trade_actions.TradeAction import TradeAction


class TradeActionOperator:

    def __call__(self, instruction: TradeActionInstruction) -> TradeActionInstruction:
        instruction.register_transform(self.operate)
        return instruction

    def operate(self, action: TradeAction) -> TradeAction:
        pass