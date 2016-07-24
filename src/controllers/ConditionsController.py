from concrete.evaluators.ConditionsEvaluator import ConditionsEvaluator
from concrete.evaluators.EffectsEvaluator import EffectsEvaluator
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from helpers.Constants import *
import pprint

from model.Move import Move


class ConditionsController(IHandler):
    def update_collector(self):
        pass

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Handling in: " + str(type(self)))
            print("Allowable moves: ")
            for moves in game_status_tmp.available_moves:
                print(moves)
                for move in game_status_tmp.available_moves[moves]:
                    pprint.pprint(vars(move))
            print("Mandatory moves: ")
            for moves in game_status_tmp.mandatory_moves:
                print(moves)
                for move in game_status_tmp.mandatory_moves[moves]:
                    pprint.pprint(vars(move))
        game_status_tmp = ConditionsController.evaluate_conditions_controller(game_status_tmp)
        if DEBUG:
            print("Allowable moves: ")
            for moves in game_status_tmp.available_moves:
                print(moves)
                for move in game_status_tmp.available_moves[moves]:
                    pprint.pprint(vars(move))
            print("Mandatory moves: ")
            for moves in game_status_tmp.mandatory_moves:
                print(moves)
                for move in game_status_tmp.mandatory_moves[moves]:
                    pprint.pprint(vars(move))
        game_status_tmp = ConditionsController.evaluate_conditions_controller(game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def evaluate_conditions_controller(game_status_tmp: GameStatus = None):
        if len(game_status_tmp.mandatory_moves) > 0:
            # check conditions for that move
            for key in game_status_tmp.mandatory_moves:
                interaction_move_list = game_status_tmp.mandatory_moves[key]
                if len(interaction_move_list) > 0:
                    move = None
                    found = False
                    for interaction_move in interaction_move_list:
                        for _move in game_status_tmp.moves:
                            if interaction_move.move_name == _move.name:
                                move = _move
                                found = True
                                break
                        if found:
                            break
                    if move is not None:
                        if len(move.conditions) > 0:
                            game_status_tmp = ConditionsController.__evaluate_condition(move, game_status_tmp)
                        else:
                            game_status_tmp = ConditionsController.__evaluate_effect(move, game_status_tmp)
        if len(game_status_tmp.available_moves) > 0:
            # check conditions for that move
            for key in game_status_tmp.mandatory_moves:
                interaction_move_list = game_status_tmp.available_moves[key]
                if len(interaction_move_list) > 0:
                    move = None
                    found = False
                    for interaction_move in interaction_move_list:
                        for _move in game_status_tmp.moves:
                            if interaction_move.move_name == _move.name:
                                move = _move
                                found = True
                                break
                        if found:
                            break
                    if move is not None:
                        if len(move.conditions) > 0:
                            game_status_tmp = ConditionsController.__evaluate_condition(move, game_status_tmp)
                        else:
                            game_status_tmp = ConditionsController.__evaluate_effect(move, game_status_tmp)
        # TODO what if first move is not defined in the principle initial scope?
        return game_status_tmp

    @staticmethod
    def __evaluate_condition(move: Move = None, game_status_tmp: GameStatus = None):
        if move is not None:
            all_conditions_satisfied = True
            for condition in move.conditions:
                # check condition setting all_conditions_satisfied to false if one of them fails
                all_conditions_satisfied = ConditionsEvaluator.evaluate(condition, game_status_tmp)
                if not all_conditions_satisfied:
                    # one of the conditions has not been met - break out
                    break
            if all_conditions_satisfied:
                game_status_tmp = ConditionsController.__evaluate_effect(move, game_status_tmp)
        return game_status_tmp

    @staticmethod
    def __evaluate_effect(move: Move = None, game_status_tmp: GameStatus = None):
        if move is not None:
            if len(move.effects) > 0:
                for effect in move.effects:
                    game_status_tmp = EffectsEvaluator.evaluate(effect, game_status_tmp)
        return game_status_tmp
