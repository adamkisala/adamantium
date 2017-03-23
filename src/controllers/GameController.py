from interface.IObservable import IObservable
from model import Game
from concrete.GameEndController import GameEndController
from concrete.data_collectors.GameStatusCollector import GameStatusCollector


class GameController(IObservable):
    game = None

    def __init__(self, game_tmp: Game = None):
        super().__init__()
        GameController.game = game_tmp
        self._listeners = []
        for player in GameController.game.players.list:
            self._listeners.append(player)
        self._game_end_controller = GameEndController()
        self._game_status_collector = GameStatusCollector(game_tmp)

    def _set_listeners(self, listeners_tmp: [] = None):
        self._listeners = listeners_tmp

    def _get_listeners(self) -> []:
        return self._listeners

    listeners = property(_get_listeners, _set_listeners, None)

    def notify_all(self):
        for listener in self.listeners:
            listener.update()

    def play(self):
        GameController.game.print_self()
        return self._game_status_collector.collect()
