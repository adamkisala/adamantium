from helpers.Constants import *
from factory.GameFactory import *
from model.Game import Game
from controllers.GameController import *
import sys


def main(argv):
    if len(sys.argv) > 0:
        file = FileStream(argv[1])
        game_fac = GameFactory()
        game = game_fac.create_game(file)
        game_controller = GameController(game)
        # game_controller.game.print_self()
        game_controller.play()

    else:
        print(NO_GAME_DESCRIPTION)


if __name__ == '__main__':
    main(sys.argv)
