from concrete.data_collectors.MoveCollector import MoveCollector
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from model.Move import Move
from enums.HandlerType import HandlerType
from helpers.Constants import *
from model.InteractionMove import InteractionMove


class MoveController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.current_speaker = self.__interaction_move.player_id
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        move_str = self.__move_collector.collect()
        self.__interaction_move = self.__parse_move(move_str)
        # TODO this move does not match really interaction move create new class with player ID update GameStatus
        # with current_speaker(the person who just did the move)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    def __init__(self):
        super().__init__()
        self.__move_collector = MoveCollector()
        self.__interaction_move = InteractionMove()

    @staticmethod
    def __parse_move(move_str: str = None) -> InteractionMove:
        # decode json and create Move
        move = InteractionMove()
        return move
