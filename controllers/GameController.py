from engine.interface import Observable
from engine.model import Game
from engine.factory import GameFactory


class GameController(Observable):
    def __init__(self, input_file):
        self.game = GameFactory.create_game(input_file)
        pass

    def notify_all(self):
        pass
