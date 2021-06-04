from backtest_execution.TradeActionInstruction import TradeActionInstruction
from backtest_execution.trade_actions.TradeAction import TradeAction


class RuleBasedAlgorithm:
    def __init__(self, instructions: list, logger):
        self.instructions = instructions
        self.logger = logger


    def decide(self, index: tuple, candle_dict: dict) -> list:
        final_action_list = []
        symbol_to_actions_mapping = {
            symbol: [] for symbol in candle_dict.keys()
        }

        instruction: TradeActionInstruction
        for instruction in self.instructions:
            new_actions = instruction.decide_actions(index=index, candle_dict=candle_dict)

            action: TradeAction
            for action in new_actions:
                symbol_to_actions_mapping[action.symbol].append(action)


        for symbol, actions in symbol_to_actions_mapping.items():
            if len(actions) == 0:
                self.logger.debug(f'No actions found for SYMBOL = {symbol} at INDEX = {index}')
            elif len(actions) == 1:
                self.logger.debug(f'Found exactly 1 ACTION for SYMBOL = {symbol} at INDEX = {index}')
                self.logger.debug(f'Adding it to final action list for INDEX = {index}')
                chosen_action = actions[0]
                final_action_list.append(chosen_action)
            else:
                self.logger.debug(f'Found exactly {len(actions)} Actions for SYMBOL = {symbol} at INDEX = {index}')
                self.logger.debug(f'Actions:')
                self.logger.debug(actions)
                chosen_action = actions[0]
                self.logger.debug(f'Adding the first one ({chosen_action}) to final action list for INDEX = {index}')


        self.logger.info(f'In total, we have {len(final_action_list)} actions for INDEX = {index}')
        self.logger.info('FINAL_ACTIONS:')
        self.logger.info(final_action_list)

        return final_action_list


