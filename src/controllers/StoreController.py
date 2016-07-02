from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus


class StoreController(IHandler):
    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        return game_status_tmp
