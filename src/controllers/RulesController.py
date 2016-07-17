from interface.IHandler import IHandler
from enums.Scope import Scope
from enums.HandlerType import HandlerType
from model.Principle import Principle
from model.GameStatus import GameStatus
from helpers.Constants import *
from concrete.evaluators.ConditionsEvaluator import ConditionsEvaluator
from concrete.evaluators.EffectsEvaluator import EffectsEvaluator


class RulesController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        principles = self.__get_principles_to_update(game_status_tmp)
        game_status_tmp = self.__evaluate_principle(principles, game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    def __get_principles_to_update(self, game_status_tmp: GameStatus = None) -> []:
        values = []
        for principle in game_status_tmp.principles:
            if principle.scope == Scope.MOVEWISE:
                if DEBUG:
                    print("Evaluating: " + str(principle))
                values.append(principle)
            elif principle.scope == Scope.TURNWISE and game_status_tmp.new_turn:
                if DEBUG:
                    print("Evaluating: " + str(principle))
                values.append(principle)
            elif principle.scope == Scope.INITIAL and game_status_tmp.initial_turn:
                if DEBUG:
                    print("Evaluating: " + str(principle))
                values.append(principle)
            else:
                if DEBUG:
                    print("Not evaluating: " + str(principle))
        return values

    def __evaluate_principle(self, principles_tmp: [] = None, game_status_tmp: GameStatus = None):
        for principle in principles_tmp:
            if DEBUG:
                print("Checking conditions of: " + str(principle))
            if len(principle.conditions) > 0:
                self.__evaluate_condition(principle, game_status_tmp)
            else:
                # just effects so evaluate them
                if len(principle.effects) > 0:
                    game_status_tmp = self.__evaluate_effect(principle, game_status_tmp)
        return game_status_tmp

    def __evaluate_condition(self, principle: Principle = None, game_status_tmp: GameStatus = None):
        if principle is not None:
            all_conditions_satisfied = True
            for condition in principle.conditions:
                # check condition setting all_conditions_satisfied to false if one of them fails
                all_conditions_satisfied = ConditionsEvaluator.evaluate(condition, game_status_tmp)
                if not all_conditions_satisfied:
                    # one of the conditions has not been met - break out
                    break
            if all_conditions_satisfied:
                game_status_tmp = self.__evaluate_effect(principle, game_status_tmp)
        return game_status_tmp

    def __evaluate_effect(self, principle: Principle = None, game_status_tmp: GameStatus = None):
        if principle is not None:
            if len(principle.effects) > 0:
                for effect in principle.effects:
                    game_status_tmp = EffectsEvaluator.evaluate(effect, game_status_tmp)
        return game_status_tmp
