import inspect

from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from helpers.Constants import *
from model.GameStatus import GameStatus


class EffectsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        effect_tmp = str(effect_tmp.name).lower()
        if effect_tmp in EffectsEvaluator.__options:
            EffectsEvaluator.__options[effect_tmp].__func__(game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __move(game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    @staticmethod
    def __store(game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    @staticmethod
    def __status(game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
            return game_status_tmp

    @staticmethod
    def __assign(game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    @staticmethod
    def __ext_effect(game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    __options = {
        "move":         __move,
        "store":        __store,
        "status":       __status,
        "assign":       __assign,
        "extEffect":    __ext_effect
    }