from interface.IGameEndController import IGameEndController
from helpers.Constants import *


class GameEndController(IGameEndController):
    def __init__(self):
        super().__init__()

    def is_finished(self, data: str = EMPTY) -> bool:
        if str.upper(data) == EXIT:
            return True
        else:
            return False
