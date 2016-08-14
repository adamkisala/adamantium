import logging

from concrete.ConsoleOutputController import ConsoleOutputController
from controllers.LoggingController import LoggingController
from interface.IHandler import IHandler
from model.GameStatus import GameStatus
from helpers.Constants import DEBUG
import pprint


class OutputController(IHandler):
    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        LoggingController.logger.debug("Handling in: " + str(type(self)))
        LoggingController.logger.debug("Game status: ")
        data = pprint.pformat(vars(game_status_tmp))
        # LoggingController.logger.info(data)
        output = ConsoleOutputController()
        output.send_output(data)
        return game_status_tmp

    def update_collector(self):
        pass

    def type(self):
        pass

    def update_flag(self):
        pass
