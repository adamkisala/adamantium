import inspect

from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class InspectEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        condition_name = str(condition_tmp.name).lower()
        if condition_name in InspectEvaluator.__options:
            evaluated = InspectEvaluator.__options[condition_name].__func__(condition_tmp, evaluated,
                                                                            game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __in(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_in(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __on(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_on(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __top(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __not_top(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    __options = {
        "In": __in,
        "!In": __not_in,
        "On": __on,
        "!On": __not_on,
        "Top": __top,
        "!Top": __not_top
    }
