from interface.IHandler import IHandler
from helpers.Constants import *
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from controllers.GameController import GameController
from enums.Role import Role


class TurnsController(IHandler):
    def handle(self, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()
        self.__turns_count = 0

    def __get_turns_count(self) -> int:
        return self.__turns_count

    turns_count = property(__get_turns_count, None, None)

    def is_max_turns(self) -> bool:
        value = False
        if GameController.game.turns.max is not None and GameController.game.turns.max > 0:
            value = True if (GameController.game.turns.max - self.turns_count <= 0) else False
        return value

    def __turn_count_increment(self):
        self.__turns_count += 1

    def get_speakers(self) -> []:
        speakers = []
        for player in GameController.game.players.list:
            if Role.SPEAKER in player.roles:
                speakers.append(player.name)
        return speakers