from interface.IHandler import IHandler
from enums.Role import Role
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType


class ConditionsController(IHandler):
    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def __init__(self):
        super().__init__()
        # self.__turns_count = 0
"""
    def __get_turns_count(self) -> int:
        return self.__turns_count

    turns_count = property(__get_turns_count, None, None)

    def is_max_turns(self) -> bool:
        value = False
        if self.game.turns.max is not None and self.game.turns.max > 0:
            value = True if (self.game.turns.max - self.turns_count <= 0) else False
        return value

    def __turn_count_increment(self):
        self.__turns_count += 1


    def get_speakers(self) -> []:
        speakers = []
        for player in self.game.players.list:
            if Role.SPEAKER in player.roles:
                speakers.append(player.name)
        return speakers
"""