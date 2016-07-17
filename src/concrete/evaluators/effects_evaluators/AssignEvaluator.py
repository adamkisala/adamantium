import inspect

from interface.IEvaluator import IEvaluator
from model.Effect import Effect
from model.GameStatus import GameStatus
from helpers.Constants import *


class AssignEvaluator(IEvaluator):
    @staticmethod
    def evaluate(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        game_status_tmp = AssignEvaluator.__evaluate_assign(effect_tmp, game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __evaluate_assign(effect_tmp: Effect = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the effect
        if len(effect_tmp.list) == 2:
            player_name = effect_tmp.list[0]
            role = effect_tmp.list[1]
            for player in game_status_tmp.players.list:
                if player_name == player.name:
                    if role not in player.roles:
                        player.roles.append(role)
                    break
        return game_status_tmp
