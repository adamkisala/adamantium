from interface.IHandler import IHandler
from helpers.Constants import *
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from enums.Magnitude import Magnitude
import controllers.GameController


class TurnsController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.initial_turn = self.__initial
        game_status_tmp.new_turn = self.__evaluate_next_player_by_turns(game_status_tmp)
        return game_status_tmp

    def update_flag(self):
        pass

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
            print("Next player: " + str(game_status_tmp.new_turn))
        return game_status_tmp

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()
        self.__multiple_moves_count = 0
        self.__initial = True

    def __get_turns_count(self) -> int:
        return self.__multiple_moves_count

    multiple_moves_count = property(__get_turns_count, None, None)

    def __turn_count_increment(self):
        self.__multiple_moves_count += 1

    def __evaluate_next_player_by_turns(self, game_status_tmp: GameStatus = None) -> bool:
        new_turn = False
        if controllers.GameController.GameController.game.turns.magnitude == Magnitude.SINGLE:
            new_turn = True
        elif controllers.GameController.GameController.game.turns.magnitude == Magnitude.MULTIPLE:
            if game_status_tmp.max_moves_per_turn is not None:
                if self.multiple_moves_count >= game_status_tmp.max_moves_per_turn:
                    new_turn = True
                    self.__multiple_moves_count = 0
                elif self.multiple_moves_count == 0:
                    new_turn = True
                    self.__turn_count_increment()
                else:
                    new_turn = False
                    self.__turn_count_increment()
            elif game_status_tmp.last_interaction_move is not None:
                if game_status_tmp.last_interaction_move.final:
                    new_turn = True
                else:
                    new_turn = False
        if game_status_tmp.all_players_did_move:
            self.__initial = False
        return new_turn
