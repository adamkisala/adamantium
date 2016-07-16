import inspect
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from helpers.Constants import *
from model.GameStatus import GameStatus


class ConditionsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        """

        :param condition_tmp: Condition
        :param game_status_tmp: GameStatus
        :return: bool
        """
        evaluated = False
        condition_name = str(condition_tmp.name).lower()
        if condition_name in ConditionsEvaluator.__options:
            evaluated = ConditionsEvaluator.__options[condition_name].__func__(evaluated)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __event(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __inspect(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __inrole(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __size(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __magnitude(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __numturns(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __corresponds(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __relation(evaluated_tmp: bool = False):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    __options = {
        "event":        __event,
        "inspect":      __inspect,
        "inrole":       __inrole,
        "size":         __size,
        "magnitude":    __magnitude,
        "numturns":     __numturns,
        "corresponds":  __corresponds,
        "relation":     __relation
    }
