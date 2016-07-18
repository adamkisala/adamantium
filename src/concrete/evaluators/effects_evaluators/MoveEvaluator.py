import inspect

from concrete.artifacts.Argument import Argument
from concrete.artifacts.Content import Content
from concrete.artifacts.Locution import Locution
from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *


class MoveEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        game_status_tmp = MoveEvaluator.__evaluate_move(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __permit(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        pass

    @staticmethod
    def __mandate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        pass

    @staticmethod
    def __next(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        pass

    @staticmethod
    def __not_next(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        pass

    @staticmethod
    def __future(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        pass

    @staticmethod
    def __not_future(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        pass

    __options = {
        "Permit": __permit,
        "Mandate": __mandate,
        "Next": __next,
        "!Next": __not_next,
        "Future": __future,
        "!Future": __not_future
    }

    @staticmethod
    def __evaluate_move(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(effect_tmp.list) >= 3:
            permit_mandate = effect_tmp.list[0]
            which_move = effect_tmp.list[1]
            move_name = effect_tmp.list[2]
            fourth_element = None
            artifact = None
            player_or_role = None
            if len(effect_tmp.list) == 4:
                fourth_element = effect_tmp.list[3]
                for player in game_status_tmp.players.list:
                    if player.name == fourth_element:
                        player_or_role = fourth_element
                if player_or_role is None:
                    for role in game_status_tmp.roles:
                        if role == fourth_element:
                            player_or_role = fourth_element
                if player_or_role is None:
                    artifact = fourth_element
            elif len(effect_tmp.list) == 5:
                artifact = effect_tmp.list[3]
                player_or_role = effect_tmp.list[4]

        return game_status_tmp
