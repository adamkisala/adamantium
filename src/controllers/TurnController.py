from controllers.GameController import GameController


class TurnsController(GameController):
    def __init__(self):
        super().__init__()
        self._turns_count = 0

    def _get_turns_count(self) -> int:
        return self._turns_count

    turns_count = property(_get_turns_count, None, None)

    def is_max_turns(self) -> bool:
        value = False
        if self.game.turns.max is not None and self.game.turns.max > 0:
            value = True if (self.game.turns.max - self.turns_count <= 0) else False
        return value

    def turn_count_increment(self):
        self._turns_count += 1

    def handle(self):
        pass
