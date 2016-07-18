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
        if len(condition_tmp.list) == 1:
            parameter = condition_tmp.list[0]
            player = game_status_tmp.players.get_player_by_name(parameter)
            if player is not None:
                if player.name in game_status_tmp.get_speakers():
                    match = True
                else:
                    match = False
            else:
                player = game_status_tmp.players.get_player_by_name(game_status_tmp.current_speaker)
                role = parameter
                if role in player.roles:
                    match = True
                else:
                    match = False
        return match
