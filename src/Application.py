import logging
import logging.config

from controllers.LoggingController import LoggingController
from helpers.Constants import *
from factory.GameFactory import *
import controllers.GameController
import sys


def main(argv):
    if len(sys.argv) > 0:

        # logger.basicConfig(filename='data.log', filemode='w', level=logging.DEBUG)
        file = FileStream(argv[1])
        game_fac = GameFactory()
        game = game_fac.create_game(file)
        game_controller = controllers.GameController.GameController(game)
        game_controller.play()

    else:
        print(NO_GAME_DESCRIPTION)


if __name__ == '__main__':
    main(sys.argv)
