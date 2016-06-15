from model import Game
from gen.dgdlListener import dgdlListener
from antlr4 import *
from gen.dgdlParser import dgdlParser
from gen.dgdlLexer import dgdlLexer


class GameFactory(dgdlListener):
    def __init__(self):
        self.game = Game

    # Enter a parse tree produced by dgdlParser#visibility.
    def enterVisibility(self, ctx: dgdlParser.VisibilityContext):
        pass

    # Enter a parse tree produced by dgdlParser#store.
    def enterStore(self, ctx: dgdlParser.StoreContext):
        pass

    # Enter a parse tree produced by dgdlParser#turns.
    def enterTurns(self, ctx:dgdlParser.TurnsContext):
        pass

    # Enter a parse tree produced by dgdlParser#visibility_type.
    def enterVisibility_type(self, ctx:dgdlParser.Visibility_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#structure_type.
    def enterStructure_type(self, ctx:dgdlParser.Structure_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#magnitude_type.
    def enterMagnitude_type(self, ctx:dgdlParser.Magnitude_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#ordering_type.
    def enterOrdering_type(self, ctx:dgdlParser.Ordering_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#players.
    def enterPlayers(self, ctx:dgdlParser.PlayersContext):
        pass

    # Enter a parse tree produced by dgdlParser#player.
    def enterPlayer(self, ctx:dgdlParser.PlayerContext):
        pass

    # Enter a parse tree produced by dgdlParser#roles.
    def enterRoles(self, ctx:dgdlParser.RolesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principles.
    def enterPrinciples(self, ctx:dgdlParser.PrinciplesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principle.
    def enterPrinciple(self, ctx:dgdlParser.PrincipleContext):
        pass

    # Enter a parse tree produced by dgdlParser#scope_type.
    def enterScope_type(self, ctx:dgdlParser.Scope_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#moves.
    def enterMoves(self, ctx:dgdlParser.MovesContext):
        pass

    # Enter a parse tree produced by dgdlParser#move.
    def enterMove(self, ctx:dgdlParser.MoveContext):
        pass

    # Enter a parse tree produced by dgdlParser#content.
    def enterContent(self, ctx:dgdlParser.ContentContext):
        pass

    # Enter a parse tree produced by dgdlParser#conditions.
    def enterConditions(self, ctx:dgdlParser.ConditionsContext):
        pass

    # Enter a parse tree produced by dgdlParser#effects.
    def enterEffects(self, ctx:dgdlParser.EffectsContext):
        pass

    # Enter a parse tree produced by dgdlParser#expr.
    def enterExpr(self, ctx:dgdlParser.ExprContext):
        pass

    # Enter a parse tree produced by dgdlParser#param.
    def enterParam(self, ctx:dgdlParser.ParamContext):
        pass

    def create_game(self, input_stream):
        lexer = dgdlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = dgdlParser(stream)
        tree = parser.game()
        listener = GameFactory()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        return self.game
