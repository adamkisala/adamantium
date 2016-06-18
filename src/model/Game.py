from model.Store import Store
from model.Turns import Turns
from model.Player import Player
from model.Players import Players


class Game:
    def __init__(self):
        self._name = None
        self._store = Store()
        self._turns = Turns()
        self._players = Players()

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _get_name(self) -> str:
        return self._name

    def _set_store(self, store_tmp: Store = None):
        self._store = store_tmp

    def _get_store(self) -> Store:
        return self._store

    def _set_turns(self, turns_tmp: Turns = None):
        self._turns = turns_tmp

    def _get_turns(self) -> Turns:
        return self._turns

    def _set_players(self, players_tmp: Players = None):
        self._players = players_tmp

    def _get_players(self) -> Players:
        return self._players

    name = property(_get_name, _set_name, None)
    store = property(_get_store, _set_store, None)
    turns = property(_get_turns, _set_turns, None)
    players = property(_get_players, _set_players, None)

    def start_game(self):
        print("Game started: " + self.name)

        print("Turns")
        print("\t" + str(self.turns.ordering))
        print("\t" + str(self.turns.magnitude))
        print("\t" + "Max: " + str(self.turns.max))

        print("Players min: " + str(self.players.min))
        print("Players max: " + str(self.players.max))

        print("Stores")
        print("Owners: " + str(self.store.owner))
        print(self.store.visibility)
        print(self.store.structure)

        pass
