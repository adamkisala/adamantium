import inspect

from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class EventEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        condition_name = str(condition_tmp.name).lower()
        if condition_name in EventEvaluator.__options:
            evaluated = EventEvaluator.__options[condition_name].__func__(condition_tmp, evaluated,
                                                                          game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __last(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_last(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __past(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_past(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    __options = {
        "last": __last,
        "!last": __not_last,
        "past": __past,
        "!past": __not_past,
    }
