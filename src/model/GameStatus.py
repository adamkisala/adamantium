from model.Game import Game
from model.InteractionMove import InteractionMove
from model.Move import Move
from enums.Role import Role
from interface.IObservable import IObservable
from helpers.Constants import *
from enums.Status import Status


class GameStatus(Game, IObservable):
    def notify_all(self):
        for listener in self.__listeners:
            listener.update(self)

    def __init__(self, game_template: Game = None):
        super().__init__()
        self.__turns_counter = 0
        self.__new_turn = False
        self.__initial_turn = True
        self.__speakers = []
        self.__current_speaker = None
        self.__last_interaction_move = None
        self.__last_move = None
        self.__available_moves = []
        self.__all_players_did_move = False
        self.__listeners = []
        self.__status = None
        if game_template is not None:
            self.name = game_template.name
            self.stores = game_template.stores
            self.turns = game_template.turns
            self.players = game_template.players
            self.roles = game_template.roles
            self.principles = game_template.principles
        for player in self.players.list:
            self.__listeners.append(player)

    def __set_new_turn(self, new_turn_tmp: bool = False):
        self.__new_turn = new_turn_tmp

    def __get_new_turn(self) -> bool:
        return self.__new_turn

    def __set_speakers(self, speakers_tmp: [] = None):
        self.__speakers = speakers_tmp

    def __get_speakers(self) -> []:
        return self.__speakers

    def __get_current_speaker(self) -> str:
        return self.__current_speaker

    def __set_current_speaker(self, speaker_tmp: str = None):
        self.__current_speaker = speaker_tmp

    def __get_current_speaker_moves(self) -> []:
        return self.__available_moves

    def __set_current_speaker_moves(self, current_speaker_moves_tmp: [] = None):
        self.__available_moves = current_speaker_moves_tmp

    def __set_initial_turn(self, initial_tmp: bool = None):
        self.__initial_turn = initial_tmp

    def __get_initial_turn(self) -> bool:
        return self.__initial_turn

    def __set_all_players_did_move(self, flag_tmp: bool = None):
        self.__all_players_did_move = flag_tmp

    def __get_all_players_did_move(self) -> bool:
        return self.__all_players_did_move

    def __get_turns_counter(self) -> int:
        return self.__turns_counter

    def __set_turns_counter(self, counter_tmp: int = 0):
        self.__turns_counter = counter_tmp

    def __set_last_interaction_move(self, last_move_tmp: InteractionMove = None):
        self.__last_interaction_move = last_move_tmp

    def __get_last_interaction_move(self) -> InteractionMove:
        return self.__last_interaction_move

    def __set_last_move(self, last_move_tmp: Move = None):
        self.__last_move = last_move_tmp

    def __get_last_move(self) -> Move:
        return self.__last_move

    def __set_status(self, status_tmp: Status = None):
        self.__status = status_tmp

    def __get_status(self) -> Status:
        return self.__status

    new_turn = property(__get_new_turn, __set_new_turn, None)
    speakers = property(__get_speakers, __set_speakers, None)
    current_speaker = property(__get_current_speaker, __set_current_speaker, None)
    available_moves = property(__get_current_speaker_moves, __set_current_speaker_moves, None)
    initial_turn = property(__get_initial_turn, __set_initial_turn, None)
    all_players_did_move = property(__get_all_players_did_move, __set_all_players_did_move, None)
    turns_counter = property(__get_turns_counter)
    last_interaction_move = property(__get_last_interaction_move, __set_last_interaction_move, None)
    last_move = property(__get_last_move, __set_last_move, None)
    status = property(__get_status, __set_status, None)

    def get_speakers(self) -> []:
        speakers = []
        for player in self.players.list:
            if Role.SPEAKER in player.roles:
                speakers.append(player.name)
        return speakers

    def set_did_move_flag(self, current_speaker: str = None):
        for player in self.players.list:
            if player.name == current_speaker:
                player.did_move_flag = True
        self.all_players_did_move = self.__update_all_players_did_move_flag()

    def __update_all_players_did_move_flag(self):
        flag = True
        for player in self.players.list:
            if player.did_move_flag is False:
                flag = False
                break
        if flag:
            self.__turns_counter += 1
            # clear flag for all
            for player in self.players.list:
                player.did_move_flag = False
            if DEBUG:
                print("New turn: " + str(self.turns_counter))
        return flag

    def set_last_move_by_name(self, move_name: str = None):
        if move_name is not None:
            for move in self.moves:
                if move_name == move.id:
                    self.last_move = move
        elif DEBUG:
            print("Could not set last_move in GameStatus")

    def __is_max_turns(self) -> bool:
        value = False
        if self.turns.max is not None and self.turns.max > 0:
            value = True if (
                self.turns.max - self.turns_counter <= 0) else False
        return value

    def evaluate_game_status(self):
        if self.__is_max_turns():
            self.__status = Status.TERMINATE

    def is_player_in_game(self, player_name: str = EMPTY):
        match = False
        for player in self.players.list:
            if player.name == player_name:
                match = True
        return match
