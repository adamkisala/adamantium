from concrete.GameEndController import GameEndController
from concrete.data_collectors.MoveCollector import MoveCollector
from controllers.LoggingController import LoggingController
from factory.ArtifactFactory import ArtifactFactory
from helpers import Constants
from helpers.StringParser import StringParser
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from model.Move import Move
from enums.HandlerType import HandlerType
from helpers.Constants import *
from model.InteractionMove import InteractionMove
import json
import logging


class MoveController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        """
        This only updates current speaker and last interaction move,
        last_move should only be updated after validation in MoveValidationController
        :param game_status_tmp:
        :return: GameStatus
        """
        if self.__interaction_move is not None:
            game_status_tmp.current_speaker = self.__interaction_move.player_name
            game_status_tmp.last_interaction_move = self.__interaction_move
        else:
            LoggingController.logger.warning("Most likely json invalid format or id returned none")
            #GameEndController.finished = True
            raise Exception(Constants.WRONG_MESSAGE_FORMAT)
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.MOVE

    def handle(self, game_status_tmp: GameStatus = None):
        move_str = self.__move_collector.collect()
        self.__interaction_move = self.__parse_move(move_str, game_status_tmp)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        return game_status_tmp

    def __init__(self):
        super().__init__()
        self.__move_collector = MoveCollector()
        self.__interaction_move = None

    @staticmethod
    def __parse_move(move_str: dict = None, game_status_tmp: GameStatus = None) -> InteractionMove:
        # decode json and create Move
        # {"move_id": "2", "move_name":"Permit", "artifact" : {"artifact_key":"Locution", "artifact_id":"1", "artifact_data":"sky is blue"}, "role":"Speaker", "final": "True"}
        if type(move_str) is not dict:
            LoggingController.logger.warning("Invalid JSON format: " + str(move_str))
            raise Exception(400, Constants.WRONG_MESSAGE_FORMAT)
        else:
            move_json = move_str
            if MOVE_ID not in move_json:
                LoggingController.logger.warning(Constants.MESSAGE_HAS_NO_ID + ": " + str(move_str))
                raise Exception(400, Constants.MESSAGE_HAS_NO_ID)
            else:
                move_id = move_json[MOVE_ID]
                move_name = move_json[MOVE_NAME] if MOVE_NAME in move_json else EMPTY
                artifact = move_json[ARTIFACT] if ARTIFACT in move_json else EMPTY
                # TODO should I be checking player or role here as well if match?
                player_name = move_json[PLAYER_NAME] if PLAYER_NAME in move_json else EMPTY
                role = move_json[ROLE] if ROLE in move_json else EMPTY
                final = move_json[FINAL] if FINAL in move_json else EMPTY
                # TODO get move from DB not from memory
                move = game_status_tmp.get_interaction_move__by_id(move_id)
                if move is not None:
                    move.artifact = ArtifactFactory.create_artifact(artifact)
                    move.final = final
                    move.player_name = player_name
                    move.role = role
                else:
                    move = InteractionMove(move_id, move_name, artifact, player_name, role, final)
        return move
