import inspect

from helpers.Helpers import Helpers
from interface.IEvaluator import IEvaluator
from model.Condition import Condition
from model.GameStatus import GameStatus
from helpers.Constants import *


# TODO ask Simon if this is about move_name or move_id
class EventEvaluator(IEvaluator):
    @staticmethod
    def evaluate(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        evaluated = EventEvaluator.__evaluate_event(condition_tmp, game_status_tmp)
        return evaluated

    def __init__(self):
        super().__init__()

    @staticmethod
    def __last(data_tmp: {} = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated = False
        if game_status_tmp.last_interaction_move is not None:
            if game_status_tmp.last_interaction_move.move_name == data_tmp['move_name']:
                evaluated = True
                artifact = data_tmp["artifact"]
                player = data_tmp["player"]
                role = data_tmp["role"]
                if artifact is not None and game_status_tmp.last_interaction_move.artifact.get_id() != artifact["id"]:
                    evaluated = False
                if player is not None and game_status_tmp.last_interaction_move.player_id != player:
                    evaluated = False
                elif role is not None and game_status_tmp.last_interaction_move.role != role:
                    evaluated = False
        return evaluated

    @staticmethod
    def __not_last(data_tmp: {} = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated = False
        if game_status_tmp.last_interaction_move is not None:
            if game_status_tmp.last_interaction_move.move_name != data_tmp['move_name']:
                evaluated = True
                artifact = data_tmp["artifact"]
                player = data_tmp["player"]
                role = data_tmp["role"]
                if artifact is not None and game_status_tmp.last_interaction_move.artifact.get_id() == artifact["id"]:
                    evaluated = False
                if player is not None and game_status_tmp.last_interaction_move.player_id == player:
                    evaluated = False
                elif role is not None and game_status_tmp.last_interaction_move.role == role:
                    evaluated = False
        return evaluated

    @staticmethod
    def __past(data_tmp: {} = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated = False
        if len(game_status_tmp.past_moves) > 0:
            for past_move in game_status_tmp.past_moves:
                if past_move.move_name == data_tmp['move_name']:
                    evaluated = True
                    artifact = data_tmp["artifact"]
                    player = data_tmp["player"]
                    role = data_tmp["role"]
                    if artifact is not None and game_status_tmp.last_interaction_move.artifact.get_id() != artifact[
                        "id"]:
                        evaluated = False
                    if player is not None and game_status_tmp.last_interaction_move.player_id != player:
                        evaluated = False
                    elif role is not None and game_status_tmp.last_interaction_move.role != role:
                        evaluated = False
                    break
        return evaluated

    @staticmethod
    def __not_past(data_tmp: {} = None, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        evaluated = True
        if len(game_status_tmp.past_moves) > 0:
            for past_move in game_status_tmp.past_moves:
                if past_move.move_name == data_tmp['move_name']:
                    evaluated = False
                    # TODO is that all checks that needs to be done here?
                    break
        return evaluated

    __options = {
        "Last": __last,
        "!Last": __not_last,
        "Past": __past,
        "!Past": __not_past,
    }

    @staticmethod
    def __evaluate_event(condition_tmp: Condition = None, game_status_tmp: GameStatus = None):
        evaluated = False
        if DEBUG:
            print("Evaluating: " + str(inspect.currentframe().f_code.co_name))
        # verify size of elements in the condition
        if len(condition_tmp.list) >= 2:
            even_type = condition_tmp.list[0]
            move_name = condition_tmp.list[1]
            fourth_element = None
            artifact = None
            player = None
            role = None
            if len(condition_tmp.list) > 2:
                if len(condition_tmp.list) == 4:
                    fourth_element = condition_tmp.list[3]
                    if Helpers.is_player(game_status_tmp, fourth_element):
                        player = fourth_element
                    elif Helpers.is_role(game_status_tmp, fourth_element):
                        role = fourth_element
                    if player is None and role is None:
                        artifact = fourth_element
                elif len(condition_tmp.list) == 5:
                    artifact = condition_tmp.list[3]
                    player_or_role = condition_tmp.list[4]
                    if Helpers.is_player(game_status_tmp, player_or_role):
                        player = fourth_element
                    elif Helpers.is_role(game_status_tmp, player_or_role):
                        role = fourth_element
            data = {"event_type": even_type, "move_name": move_name, "artifact": artifact, "player": player,
                    "role": role}
            if even_type in EventEvaluator.__options:
                evaluated = EventEvaluator.__options[even_type].__func__(data, game_status_tmp)
        return evaluated
