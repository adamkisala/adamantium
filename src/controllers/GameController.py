from interface.IObservable import IObservable
from model import Game


class GameController(IObservable):
    def __init__(self, game_tmp: Game = None):
        super().__init__()
        self._game = game_tmp

    def _get_game(self) -> Game:
        return self._game

    def _set_game(self, game_tmp: Game = None):
        self._game = game_tmp

    game = property(_get_game, None, None)

    def notify_all(self):
        pass
