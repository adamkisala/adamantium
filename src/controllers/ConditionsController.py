import logging

from concrete.evaluators.ConditionsEvaluator import ConditionsEvaluator
from concrete.evaluators.EffectsEvaluator import EffectsEvaluator
from controllers.LoggingController import LoggingController
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from helpers.Constants import *
import pprint

from model.Move import Move


class ConditionsController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.speakers = game_status_tmp.get_speakers()
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = ConditionsController.evaluate_conditions_controller(game_status_tmp)
        logger = ''
        logger += ("Handling in: " + str(type(self)) + "\n")
        logger += "Allowable moves: " + "\n"
        for moves in game_status_tmp.available_moves:
            logger += str(moves) + "\n"
            for move in game_status_tmp.available_moves[moves]:
                logger += pprint.pformat(vars(move)) + "\n"
        logger += "Mandatory moves: " + "\n"
        for moves in game_status_tmp.mandatory_moves:
            logger += str(moves) + "\n"
            for move in game_status_tmp.mandatory_moves[moves]:
                logger += pprint.pformat(vars(move)) + "\n"
        LoggingController.logger.debug(logger)
        game_status_tmp = self.update_collector(game_status_tmp)
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def evaluate_conditions_controller(game_status_tmp: GameStatus = None):
        if len(game_status_tmp.mandatory_moves) > 0:
            # check conditions for that move
            moves_not_meeting_conditions = []
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
                        all_conditions_satisfied = True
                        if len(move.conditions) > 0:
                            all_conditions_satisfied = ConditionsController.__evaluate_condition(move, game_status_tmp)
                        if not all_conditions_satisfied:
                            moves_not_meeting_conditions.append(move)
                for move in moves_not_meeting_conditions:
                    interaction_move_list.remove(move)
        if len(game_status_tmp.available_moves) > 0:
            # check conditions for that move
            for key in game_status_tmp.mandatory_moves:
                moves_not_meeting_conditions = []
                interaction_move_list = game_status_tmp.available_moves[key]
                if len(interaction_move_list) > 0:
                    move = None
                    interaction_move_to_delete = None
                    found = False
                    for interaction_move in interaction_move_list:
                        for _move in game_status_tmp.moves:
                            if interaction_move.move_name == _move.name:
                                interaction_move_to_delete = interaction_move
                                move = _move
                                found = True
                                break
                        if found:
                            break
                    if move is not None:
                        all_conditions_satisfied = True
                        if len(move.conditions) > 0:
                            all_conditions_satisfied = ConditionsController.__evaluate_condition(move, game_status_tmp)
                        if not all_conditions_satisfied:
                            moves_not_meeting_conditions.append(interaction_move_to_delete)
                for move in moves_not_meeting_conditions:
                    interaction_move_list.remove(move)
        return game_status_tmp

    @staticmethod
    def __evaluate_condition(move: Move = None, game_status_tmp: GameStatus = None):
        all_conditions_satisfied = True
        if move is not None:
            for condition in move.conditions:
                # check condition setting all_conditions_satisfied to false if one of them fails
                all_conditions_satisfied = ConditionsEvaluator.evaluate(condition, game_status_tmp)
                if not all_conditions_satisfied:
                    # one of the conditions has not been met - break out
                    break
        return all_conditions_satisfied
