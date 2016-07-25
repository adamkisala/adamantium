from concrete.data_collectors.MoveCollector import MoveCollector
from factory.ArtifactFactory import ArtifactFactory
from helpers.StringParser import StringParser
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
        if self.__interaction_move is not None:
            if DEBUG:
                print(str(self.__interaction_move) + " Move id: " + str(self.__interaction_move.move_id))
            game_status_tmp.current_speaker = self.__interaction_move.player_name
            game_status_tmp.last_interaction_move = self.__interaction_move
        else:
            if DEBUG:
                print("Most likely json invalid format or id returned none")
            # TODO raise error
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        if DEBUG:
            print("Handling in: " + str(type(self)))
        move_str = self.__move_collector.collect()
        self.__interaction_move = self.__parse_move(move_str, game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        return game_status_tmp

    def __init__(self):
        super().__init__()
        self.__move_collector = MoveCollector()
        self.__interaction_move = InteractionMove()

    def __parse_move(self, move_str: str = None, game_status_tmp: GameStatus = None) -> InteractionMove:
        # decode json and create Move
        # {"move_id": "2", "move_name":"Permit", "artifact" : {"artifact_key":"Locution", "artifact_id":"1", "artifact_data":"sky is blue"}, "player_name":"Adam", "final": "True"}
        if StringParser.is_json(move_str):
            move_json = json.loads(StringParser.dict_to_string(move_str))
            if 'move_id' in move_json:
                move_id = move_json[MOVE_ID]
                move_name = move_json[MOVE_NAME] if MOVE_NAME in move_json else EMPTY
                artifact = move_json[ARTIFACT] if ARTIFACT in move_json else EMPTY
                # TODO should I be checking player or role here as well if match? move_id should be enough
                player_name = move_json[PLAYER_NAME] if PLAYER_NAME in move_json else EMPTY
                role = move_json[ROLE] if ROLE in move_json else EMPTY
                final = move_json[FINAL] if FINAL in move_json else EMPTY
                move = game_status_tmp.get_interaction_move__by_id(move_id)
                if move is not None:
                    move.artifact = ArtifactFactory.create_artifact(artifact)
                    move.final = final
                    move.player_name = player_name
                    move.role = role
            else:
                move = None
        else:
            move = None
            if DEBUG:
                print("Invalid JSON format: " + move_str)
                # TODO raise error
        return move
