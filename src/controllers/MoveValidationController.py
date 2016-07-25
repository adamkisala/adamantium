from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *
from controllers.MoveController import MoveController


class MoveValidationController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.set_did_move_flag(game_status_tmp.current_speaker)
        # TODO this is to be done after validation that the move was correct
        if game_status_tmp.last_interaction_move:
            game_status_tmp.set_last_move_by_name(game_status_tmp.last_interaction_move.move_name)
            game_status_tmp.past_moves.append(game_status_tmp.last_interaction_move)
        else:
            if DEBUG:
                print("game_status_tmp.last_interaction_move: None\n\tLast move could not be parsed")
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        valid = MoveValidationController.__validate(game_status_tmp)
        if valid:
            game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    def __init__(self):
        super().__init__()

    @staticmethod
    def __validate(game_status_tmp: GameStatus = None):
        valid = False
        if game_status_tmp.last_interaction_move:
            # check mandatory moves first
            # TODO check with Simon
            if len(game_status_tmp.mandatory_moves) > 0:
                # check by move_id
                for key in game_status_tmp.mandatory_moves:
                    for interaction_move in game_status_tmp.mandatory_moves[key]:
                        if interaction_move.move_id == game_status_tmp.last_interaction_move.move_id:
                            if interaction_move.player_id in game_status_tmp.get_speakers():
                                valid = True
                                break
                    if valid:
                        break
            # check available moves
            if len(game_status_tmp.available_moves) > 0:
                # check by move_id
                for key in game_status_tmp.available_moves:
                    for interaction_move in game_status_tmp.available_moves[key]:
                        if interaction_move.move_id == game_status_tmp.last_interaction_move.move_id:
                            if interaction_move.player_id in game_status_tmp.get_speakers():
                                valid = True
                                break
                    if valid:
                        break
        return valid
