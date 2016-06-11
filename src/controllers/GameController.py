from interface import Observable
from model import Game
from factory import GameFactory


class GameController(Observable):
    def __init__(self, input_file):
        self.game = GameFactory.create_game(input_file)
        pass

    def notify_all(self):
        pass
