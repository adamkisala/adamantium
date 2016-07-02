from concrete.data_collectors.MoveCollector import MoveCollector
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from model.Move import Move
from enums.HandlerType import HandlerType


class MoveController(IHandler):
    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        move_str = self.__move_collector.collect()
        self.__move = self.__parse_move(move_str)
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
