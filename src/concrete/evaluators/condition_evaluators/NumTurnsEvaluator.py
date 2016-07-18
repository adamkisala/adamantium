import inspect

from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class NumTurnsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = NumTurnsEvaluator.__check_numturns(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __check_numturns(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        evaluated_tmp = False
        # verify size of elements in the condition
        if len(condition_tmp.list) == 2:
            system_name = condition_tmp.list[0]
            number = condition_tmp.list[1]
            if system_name == game_status_tmp.name and game_status_tmp.turns_counter == number:
                evaluated_tmp = True
        return evaluated_tmp
