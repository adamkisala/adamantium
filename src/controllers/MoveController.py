from concrete.data_collectors.MoveCollector import MoveCollector
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from model.Move import Move
from enums.HandlerType import HandlerType
from helpers.Constants import *


class MoveController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        move_str = self.__move_collector.collect()
        self.__move = self.__parse_move(move_str)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    def __init__(self):
        super().__init__()
        self.__move_collector = MoveCollector()
        self.__move = Move()

    @staticmethod
    def __parse_move(move_str: str = None) -> Move:
        # decode json and create Move
        move = Move()
        return move
