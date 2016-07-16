import inspect

from concrete.evaluators.condition_evaluators.EventEvaluator import EventEvaluator
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
            evaluated = ConditionsEvaluator.__options[condition_name].__func__(condition_tmp, evaluated, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __event(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated_tmp = EventEvaluator.evaluate(condition_tmp, game_status_tmp)
        return evaluated_tmp

    @staticmethod
    def __inspect(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __inrole(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __size(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __magnitude(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __numturns(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __corresponds(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return evaluated_tmp

    @staticmethod
    def __relation(condition_tmp: Condition = None, evaluated_tmp: bool = False, game_status_tmp: GameStatus = None):
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
