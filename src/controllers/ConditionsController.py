from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from helpers.Constants import *
import pprint


class ConditionsController(IHandler):
    def update_collector(self):
        pass

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Handling in: " + str(type(self)))
            print("Allowable moves: ")
            pprint.pprint(game_status_tmp.available_moves)
            print("Mandatory moves: ")
            pprint.pprint(game_status_tmp.mandatory_moves)
        return game_status_tmp

    def __init__(self):
        super().__init__()
