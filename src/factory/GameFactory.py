from model.Game import Game
from model.Store import Store
from gen.dgdlListener import dgdlListener
from antlr4 import *
from gen.dgdlParser import dgdlParser
from gen.dgdlLexer import dgdlLexer
from enums.Magnitude import *
from enums.Ordering import *
from enums.Scope import *
from enums.Structure import *


class GameFactory(dgdlListener):
    game = Game()

    def __init__(self):
        pass

    # Enter a parse tree produced by dgdlParser#store.
    def enterStore(self, ctx: dgdlParser.StoreContext):
        pass

    # Enter a parse tree produced by dgdlParser#turns.
    def enterTurns(self, ctx: dgdlParser.TurnsContext):
        pass

    # Enter a parse tree produced by dgdlParser#visibility_type.
    def enterVisibility_type(self, ctx: dgdlParser.Visibility_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#structure_type.
    def enterStructure_type(self, ctx: dgdlParser.Structure_typeContext):
        if str(ctx.getText()) == str(ctx.STACK()):
            GameFactory.game.store.structure = Structure.STACK
        elif str(ctx.getText()) == str(ctx.SET()):
            GameFactory.game.store.structure = Structure.SET
        elif str(ctx.getText()) == str(ctx.QUEUE()):
            GameFactory.game.store.structure = Structure.QUEUE

    # Enter a parse tree produced by dgdlParser#magnitude_type.
    def enterMagnitude_type(self, ctx: dgdlParser.Magnitude_typeContext):
        if str(ctx.getText()) == str(ctx.SINGLE()):
            GameFactory.game.turns.magnitude = Magnitude.SINGLE
            print(GameFactory.game.turns.magnitude)
        elif str(ctx.getText()) == str(ctx.MULTIPLE()):
            GameFactory.game.turns.magnitude = Magnitude.MULTIPLE
            print(GameFactory.game.turns.magnitude)

    # Enter a parse tree produced by dgdlParser#ordering_type.
    def enterOrdering_type(self, ctx: dgdlParser.Ordering_typeContext):
        if str(ctx.getText()) == str(ctx.STRICT()):
            GameFactory.game.turns.ordering = Ordering.STRICT
        elif str(ctx.getText()) == str(ctx.LIBERAL()):
            GameFactory.game.turns.ordering = Ordering.LIBERAL

    # Enter a parse tree produced by dgdlParser#players.
    def enterPlayers(self, ctx: dgdlParser.PlayersContext):
        pass

    # Enter a parse tree produced by dgdlParser#player.
    def enterPlayer(self, ctx: dgdlParser.PlayerContext):
        pass

    # Enter a parse tree produced by dgdlParser#roles.
    def enterRoles(self, ctx: dgdlParser.RolesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principles.
    def enterPrinciples(self, ctx: dgdlParser.PrinciplesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principle.
    def enterPrinciple(self, ctx: dgdlParser.PrincipleContext):
        pass

    # Enter a parse tree produced by dgdlParser#scope_type.
    def enterScope_type(self, ctx: dgdlParser.Scope_typeContext):
        pass

    # Enter a parse tree produced by dgdlParser#moves.
    def enterMoves(self, ctx: dgdlParser.MovesContext):
        pass

    # Enter a parse tree produced by dgdlParser#move.
    def enterMove(self, ctx: dgdlParser.MoveContext):
        pass

    # Enter a parse tree produced by dgdlParser#content.
    def enterContent(self, ctx: dgdlParser.ContentContext):
        pass

    # Enter a parse tree produced by dgdlParser#conditions.
    def enterConditions(self, ctx: dgdlParser.ConditionsContext):
        pass

    # Enter a parse tree produced by dgdlParser#effects.
    def enterEffects(self, ctx: dgdlParser.EffectsContext):
        pass

    # Enter a parse tree produced by dgdlParser#expr.
    def enterExpr(self, ctx: dgdlParser.ExprContext):
        pass

    # Enter a parse tree produced by dgdlParser#param.
    def enterParam(self, ctx: dgdlParser.ParamContext):
        pass

    @staticmethod
    def create_game(input_stream):
        lexer = dgdlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = dgdlParser(stream)
        tree = parser.game()
        listener = GameFactory()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)


