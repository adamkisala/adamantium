import inspect

from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


class InroleEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = InroleEvaluator.__check_inrole(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __check_inrole(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        match = False
        # check number of parameters supplied
        if len(condition_tmp.list) == 2:
            player_name = condition_tmp.list[0]
            role = condition_tmp.list[1]
            player = game_status_tmp.players.get_player_by_name(player_name)
            if player is not None:
                if role in player.roles:
                    match = True
        return match
