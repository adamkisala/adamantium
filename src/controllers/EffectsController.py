from concrete.evaluators.EffectsEvaluator import EffectsEvaluator
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *


class EffectsController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = EffectsController.__evaluate_effects(game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    @staticmethod
    def __evaluate_effects(game_status_tmp: GameStatus = None):
        if game_status_tmp.last_move:
            if len(game_status_tmp.last_move.effects) > 0:
                for effect in game_status_tmp.last_move.effects:
                    # TODO need to check what condition it is and substitute data in effect
                    game_status_tmp = EffectsEvaluator.evaluate(effect, game_status_tmp)
        return game_status_tmp
