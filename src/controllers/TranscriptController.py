import logging
import logging.config

from controllers.LoggingController import LoggingController
from interface.IHandler import IHandler
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *


class TranscriptController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.POST_MOVE_CHECK

    def handle(self, game_status_tmp: GameStatus = None):
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        LoggingController.logger.debug("Handling in: " + str(type(self)))
        return game_status_tmp

    def __init__(self):
        super().__init__()
