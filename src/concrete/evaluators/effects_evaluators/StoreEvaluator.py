import inspect

from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *


class StoreEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        game_status_tmp = StoreEvaluator.__evaluate_store(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __add(game_status_tmp: GameStatus = None, commitment: str = EMPTY, store_name: str = EMPTY,
              player_or_role: str = EMPTY):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))

        return game_status_tmp

    @staticmethod
    def __remove(game_status_tmp: GameStatus = None, commitment: str = EMPTY, store_name: str = EMPTY,
                 player_or_role: str = EMPTY):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        return game_status_tmp

    __options = {
        "add": __add,
        "remove": __remove
    }

    @staticmethod
    def __evaluate_store(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(effect_tmp.list) == 4:
            action = effect_tmp.list[0]
            commitment = effect_tmp.list[1]
            store_name = effect_tmp.list[2]
            player_or_role = effect_tmp.list[3]
            if action in StoreEvaluator.__options:
                game_status_tmp = StoreEvaluator.__options[action].__func__(game_status_tmp, commitment, store_name,
                                                                            player_or_role)
        return game_status_tmp
