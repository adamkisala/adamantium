from interface.IHandler import IHandler
from helpers.Constants import *
from model.GameStatus import GameStatus
from enums.HandlerType import HandlerType
from enums.Magnitude import Magnitude
import controllers.GameController


class TurnsController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        game_status_tmp.initial_turn = self.__initial
        game_status_tmp.new_turn = self.__evaluate_new_turn(game_status_tmp)
        return game_status_tmp

    def update_flag(self):
        pass

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
            print("New turn: " + str(game_status_tmp.new_turn))
        return game_status_tmp

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()
        self.__turns_count = 0
        self.__initial = True

    def __get_turns_count(self) -> int:
        return self.__turns_count

    turns_count = property(__get_turns_count, None, None)

    def is_max_turns(self) -> bool:
        value = False
        if controllers.GameController.GameController.game.turns.max is not None and controllers.GameController.GameController.game.turns.max > 0:
            value = True if (
                controllers.GameController.GameController.game.turns.max - self.turns_count <= 0) else False
        return value

    def __turn_count_increment(self):
        self.__turns_count += 1

    def __evaluate_new_turn(self, game_status_tmp: GameStatus = None) -> bool:
        new_turn = False
        if controllers.GameController.GameController.game.turns.magnitude == Magnitude.SINGLE:
            new_turn = True
            self.__turns_count = 0
            game_status_tmp.set_did_move_flag_(game_status_tmp.current_speaker)
            if game_status_tmp.all_players_did_move:
                self.__initial = False
        elif controllers.GameController.GameController.game.turns.magnitude == Magnitude.MULTIPLE:
            if controllers.GameController.GameController.game.turns.max is not None and controllers.GameController.GameController.game.turns.max > 0:
                if self.turns_count >= controllers.GameController.GameController.game.turns.max:
                    new_turn = True
                    self.__turns_count = 0
                    game_status_tmp.set_did_move_flag_(game_status_tmp.current_speaker)
                    if game_status_tmp.all_players_did_move:
                        self.__initial = False
                elif self.turns_count == 0:
                    new_turn = True
                    self.__turn_count_increment()
                    game_status_tmp.set_did_move_flag_(game_status_tmp.current_speaker)
                    if game_status_tmp.all_players_did_move:
                        self.__initial = False
                else:
                    new_turn = False
                    self.__turn_count_increment()
            else:
                move = game_status_tmp.moves[len(game_status_tmp.moves) - 1]
                if move.final:
                    new_turn = True
                    self.__turns_count = 0
                    game_status_tmp.set_did_move_flag_(game_status_tmp.current_speaker)
                    if game_status_tmp.all_players_did_move:
                        self.__initial = False
                else:
                    new_turn = False
                    self.__turn_count_increment()
        return new_turn
