from model.Game import Game
from model.Player import Player
from enums.Role import Role
from interface.IObservable import IObservable


class GameStatus(Game, IObservable):
    def notify_all(self):
        for listener in self.__listeners:
            listener.update(self)

    def __init__(self, game_template: Game = None):
        super().__init__()
        self.__new_turn = False
        self.__initial_turn = True
        self.__speakers = []
        self.__current_speaker = None
        self.__available_moves = []
        self.__all_players_did_move = False
        self.__listeners = []
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

    new_turn = property(__get_new_turn, __set_new_turn, None)
    speakers = property(__get_speakers, __set_speakers, None)
    current_speaker = property(__get_current_speaker, __set_current_speaker, None)
    available_moves = property(__get_current_speaker_moves, __set_current_speaker_moves, None)
    initial_turn = property(__get_initial_turn, __set_initial_turn, None)
    all_players_did_move = property(__get_all_players_did_move, __set_all_players_did_move, None)

    def get_speakers(self) -> []:
        speakers = []
        for player in self.players.list:
            if Role.SPEAKER in player.roles:
                speakers.append(player.name)
        return speakers

    def set_did_move_flag_(self, current_speaker: str = None):
        for player in self.players.list:
            if player.name == current_speaker:
                player.did_move_flag = True
        self.__update_all_players_did_move_flag()

    def __update_all_players_did_move_flag(self):
        flag = True
        for player in self.players.list:
            if player.did_move_flag is False:
                flag = False
                break
        return flag
