from antlr4 import *
from gen.dgdlParser import dgdlParser
from gen.dgdlLexer import dgdlLexer
from gen.dgdlListener import dgdlListener
from helpers.Constants import *
import sys


def main(argv):
    if len(sys.argv) > 0:
        file = FileStream(argv[1])
        lexer = dgdlLexer(file)
        stream = CommonTokenStream(lexer)
        parser = dgdlParser(stream)
        tree = parser.game()
        listener = dgdlListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
    else:
        print(NO_GAME_DESCRIPTION)

if __name__ == '__main__':
    main(sys.argv)
