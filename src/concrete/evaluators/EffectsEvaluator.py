import inspect

from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from helpers.Constants import *
from model.GameStatus import GameStatus


class EffectsEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        effect_tmp = str(effect_tmp.name)
        if effect_tmp in EffectsEvaluator.__options:
            game_status_tmp = EffectsEvaluator.__options[effect_tmp].__func__(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __move(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    @staticmethod
    def __store(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    @staticmethod
    def __status(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
            return game_status_tmp

    @staticmethod
    def __assign(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    @staticmethod
    def __ext_effect(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    __options = {
        "Move":         __move,
        "Store":        __store,
        "Status":       __status,
        "Assign":       __assign,
        "ExtEffect":    __ext_effect
    }