from helpers.Constants import *
from factory.GameFactory import *
from model.Game import Game
import sys


def main(argv):
    if len(sys.argv) > 0:
        file = FileStream(argv[1])
        game_fac = GameFactory()
        game_fac.create_game(file)
        game_fac.game.start_game()
    else:
        print(NO_GAME_DESCRIPTION)


if __name__ == '__main__':
    main(sys.argv)
