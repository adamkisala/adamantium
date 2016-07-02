from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *


class RulesController(IHandler):
    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp
