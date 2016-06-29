from model.Store import Store
from model.Turns import Turns
from model.Player import Player
from model.Players import Players
from model.Principle import Principle
from model.Move import Move


class Game:
    def __init__(self):
        self._name = None
        self._store = []
        self._turns = Turns()
        self._players = Players()
        self._roles = []
        self._principles = []
        self._moves = []

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _get_name(self) -> str:
        return self._name

    def _set_store(self, store_tmp: [] = None):
        self._store = store_tmp

    def _get_store(self) -> []:
        return self._store

    def _set_turns(self, turns_tmp: Turns = None):
        self._turns = turns_tmp

    def _get_turns(self) -> Turns:
        return self._turns

    def _set_players(self, players_tmp: Players = None):
        self._players = players_tmp

    def _get_players(self) -> Players:
        return self._players

    def _get_roles(self) -> []:
        return self._roles

    def _set_roles(self, roles_tmp: [] = None):
        self._roles = roles_tmp

    def _get_principles(self) -> []:
        return self._principles

    def _set_principles(self, principles_tmp: [] = None):
        self._principles = principles_tmp

    def _set_moves(self, moves_tmp: [] = None):
        self._moves = moves_tmp

    def _get_moves(self) -> []:
        return self._moves

    name = property(_get_name, _set_name, None)
    stores = property(_get_store, _set_store, None)
    turns = property(_get_turns, _set_turns, None)
    players = property(_get_players, _set_players, None)
    roles = property(_get_roles, _set_roles, None)
    principles = property(_get_principles, _set_principles, None)
    moves = property(_get_moves, _set_moves, None)

    def start_game(self):
        print("Game started: " + self.name)

        print("Turns")
        print("\t" + str(self.turns.ordering))
        print("\t" + str(self.turns.magnitude))
        print("\t" + "Max: " + str(self.turns.max))

        print("Players min: " + str(self.players.min))
        print("Players max: " + str(self.players.max))
        print("Players: ")
        for player in self.players.list:
            print("\t" + player.name)
            print("\t" + str(player.roles))

        print("Stores")
        for store in self.stores:
            print("\t" + store.name)
            print("\t" + "Owners: " + str(store.owner))
            print("\t" + str(store.visibility))
            print("\t" + str(store.structure))

        print("Roles:")
        for role in self.roles:
            print("\t" + str(role))

        print("Principles:")
        for principle in self.principles:
            print("\t" + principle.name)
            print("\t" + str(principle.scope))
            for condition in principle.conditions:
                print("\t" + "\t" + condition.name)
                print("\t" + "\t" + str(condition.list))
            for effect in principle.effects:
                print("\t" + "\t" + effect.name)
                print("\t" + "\t" + str(effect.list))

        print("Moves:")
        for move in self.moves:
            print("\t" + move.name)
            print("\t" + "\t" + "Content: " + str(move.content.list))
            for condition in move.conditions:
                print("\t" + "\t" + condition.name)
                print("\t" + "\t" + str(condition.list))
            for effect in move.effects:
                print("\t" + "\t" + effect.name)
                print("\t" + "\t" + str(effect.list))