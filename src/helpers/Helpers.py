from model.GameStatus import GameStatus
from helpers.Constants import *


class Helpers:
    @staticmethod
    def is_player(game_status_tmp: GameStatus = None, player_or_role: str = EMPTY):
        player = False
        for _player in game_status_tmp.players.list:
            if _player.name == player_or_role:
                player = True
        return player

    @staticmethod
    def is_role(game_status_tmp: GameStatus = None, player_or_role: str = EMPTY):
        role = False
        for _role in game_status_tmp.roles:
            if _role == player_or_role:
                role = True
        return role
