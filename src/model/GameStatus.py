from model.Game import Game
from model.Player import Player
from enums.Role import Role


class GameStatus(Game):
    def __init__(self, game_template: Game = None):
        super().__init__()
        self.__new_turn = False
        self.__speakers = []
        self.__current_speaker = Player()
        self.__current_speaker_moves = []
        if game_template is not None:
            self.name = game_template.name
            self.stores = game_template.stores
            self.turns = game_template.turns
            self.players = game_template.players
            self.roles = game_template.roles
            self.principles = game_template.principles

    def __set_new_turn(self, new_turn_tmp: bool = False):
        self.__new_turn = new_turn_tmp

    def __get_new_turn(self) -> bool:
        return self.__new_turn

    def __set_speakers(self, speakers_tmp: [] = None):
        self.__speakers = speakers_tmp

    def __get_speakers(self) -> []:
        return self.__speakers

    def __get_current_speaker(self) -> Player:
        return self.__current_speaker

    def __set_current_speaker(self, speaker_tmp: Player = None):
        self.__current_speaker = speaker_tmp

    def __get_current_speaker_moves(self) -> []:
        return self.__current_speaker_moves

    def __set_current_speaker_moves(self, currnet_speaker_moves_tmp: [] = None):
        self.__current_speaker_moves = currnet_speaker_moves_tmp

    new_turn = property(__get_new_turn, __set_new_turn, None)
    speakers = property(__get_speakers, __set_speakers, None)
    current_speaker = property(__get_current_speaker, __set_current_speaker, None)
    current_speaker_moves = property(__get_current_speaker_moves, __set_current_speaker_moves, None)

    def get_speakers(self) -> []:
        speakers = []
        for player in self.players.list:
            if Role.SPEAKER in player.roles:
                speakers.append(player.name)
        return speakers
