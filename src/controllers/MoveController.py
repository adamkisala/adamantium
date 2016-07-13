from concrete.data_collectors.MoveCollector import MoveCollector
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from model.Move import Move
from enums.HandlerType import HandlerType
from helpers.Constants import *
from model.InteractionMove import InteractionMove
import json


class MoveController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        """
        This only updates current speaker and last interaction move,
        last_move should only be updated after validation in MoveValidationController
        :param game_status_tmp:
        :return: GameStatus
        """
        game_status_tmp.current_speaker = self.__interaction_move.player_id
        game_status_tmp.last_interaction_move = self.__interaction_move
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        move_str = self.__move_collector.collect()
        self.__interaction_move = self.__parse_move(move_str)
        # TODO this move does not match really interaction move create new class with player ID update GameStatus
        # with current_speaker(the person who just did the move)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
            print(str(self.__interaction_move) + " Move id: " + str(self.__interaction_move.move_id))
            print(self.__interaction_move)
        return game_status_tmp

    def __init__(self):
        super().__init__()
        self.__move_collector = MoveCollector()
        self.__interaction_move = InteractionMove()

    def __parse_move(self, move_str: str = None, game_status_tmp: GameStatus = None) -> InteractionMove:
        # decode json and create Move
        # {"move_type":"permit", "content":"stufff", "player_id":"White", "role":"speaker", "final": "True"}
        if self.__is_json(move_str):
            move_json = json.loads(str(move_str))
            move = InteractionMove(**move_json)
        else:
            move = InteractionMove()
            if DEBUG:
                print("Invalid JSON format: " + move_str)
            # TODO raise error
        return move

    def __is_json(self, json_str: str = EMPTY):
        try:
            json.loads(json_str)
        except ValueError:
            return False
        return True

