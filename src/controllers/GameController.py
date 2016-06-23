from interface.IObservable import IObservable
from model import Game
from interface.IGameObserver import IGameObserver


class GameController(IObservable):
    def __init__(self, game_tmp: Game = None):
        super().__init__()
        self._game = game_tmp
        self._listeners = [IGameObserver]
        for player in self.game.players.list:
            self.listeners.append(player)

    def _get_game(self) -> Game:
        return self._game

    def _set_game(self, game_tmp: Game = None):
        self._game = game_tmp

    def _set_listeners(self, listeners_tmp: [] = None):
        self._listeners = listeners_tmp

    def _get_listeners(self) -> []:
        return self._listeners

    game = property(_get_game, None, None)
    listeners = property(_get_listeners, _set_listeners, None)

    def notify_all(self):
        for listener in self.listeners:
            listener.update()
