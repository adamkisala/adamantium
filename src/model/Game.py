from model.Store import Store
from model.Turns import Turns


class Game:
    def __init__(self):
        self.store = Store()
        self.turns = Turns()

    def start_game(self):
        print("Game started")
        print(self.turns.magnitude)
        pass

