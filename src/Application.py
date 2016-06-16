from antlr4 import *
from gen.dgdlParser import dgdlParser
from gen.dgdlLexer import dgdlLexer
from gen.dgdlListener import dgdlListener
from helpers.Constants import *
from factory.GameFactory import *
from model.Game import Game
import sys


def main(argv):
    if len(sys.argv) > 0:
        file = FileStream(argv[1])
        GameFactory.create_game(file)
        print(GameFactory.game.turns.magnitude)
    else:
        print(NO_GAME_DESCRIPTION)


if __name__ == '__main__':
    main(sys.argv)
