from model.Game import Game
from model.Player import Player
from model.Store import Store
from gen.dgdlListener import dgdlListener
from antlr4 import *
from gen.dgdlParser import dgdlParser
from gen.dgdlLexer import dgdlLexer
from enums.Structure import Structure
from enums.Visibility import Visibility
from enums.Magnitude import Magnitude
from enums.Ordering import Ordering
from enums.Scope import *
from helpers.StringParser import *
from helpers.Constants import *


class GameFactory(dgdlListener):
    def __init__(self, game_temp: Game = Game()):
        self._game = game_temp
        pass

    def _get_game(self) -> Game:
        return self._game

    game = property(_get_game, None, None, "Game object created by factory")

    # Enter a parse tree produced by dgdlParser#game.
    def enterGame(self, ctx: dgdlParser.GameContext):
        data = str(ctx.getText())
        if str(ctx.IDENT()) in data:
            self.game.name = StringParser.before(data, OPEN_BRACE)

    # Enter a parse tree produced by dgdlParser#store.
    def enterStore(self, ctx: dgdlParser.StoreContext):
        data = str(ctx.getText())
        store = Store()
        if str(ctx.NAME()) in data:
            store.name = StringParser.between(data, str(ctx.NAME()) + COLON, COMMA)
        if str(ctx.OWNER()) in data:
            values = StringParser.between(data, str(ctx.OWNER()) + OPEN_BRACE, CLOSE_BRACE)
            store.owner = values.split(",")
        if str(ctx.STRUCTURE()) in data:
            store.structure = StringParser.between(data, str(ctx.STRUCTURE()) + COLON, COMMA)
        if str(ctx.VISIBILITY()) in data:
            store.visibility = StringParser.between(data, str(ctx.VISIBILITY()) + COLON, CLOSE_BRACE)
        self.game.stores.append(store)

    # Enter a parse tree produced by dgdlParser#turns.
    def enterTurns(self, ctx: dgdlParser.TurnsContext):
        data = str(ctx.getText())
        if str(ctx.MAX()) in data:
            self.game.turns.max = int(StringParser.between(data, str(ctx.MAX()) + COLON, CLOSE_BRACE))
        if str(ctx.MAGNITUDE()) in data:
            self.game.turns.magnitude = StringParser.between(data, str(ctx.MAGNITUDE()) + COLON, COMMA)
        if str(ctx.ORDERING()) in data:
            self.game.turns.ordering = StringParser.between(data, str(ctx.ORDERING()) + COLON,
                                                            COMMA if (str(ctx.MAX()) in data) else CLOSE_BRACE)

    # Enter a parse tree produced by dgdlParser#players.
    def enterPlayers(self, ctx: dgdlParser.PlayersContext):
        data = str(ctx.getText())
        if str(ctx.MIN()) in data:
            self.game.players.min = int(
                StringParser.between(data, str(ctx.MIN()) + COLON, COMMA if (str(ctx.MAX()) in data) else CLOSE_BRACE))
        if str(ctx.MAX()) in data:
            self.game.players.max = int(StringParser.between(data, str(ctx.MAX()) + COLON, CLOSE_BRACE))

    # Enter a parse tree produced by dgdlParser#player.
    def enterPlayer(self, ctx: dgdlParser.PlayerContext):
        data = str(ctx.getText())
        player = Player()
        if str(ctx.NAME()) in data:
            player.name = StringParser.between(data, str(ctx.NAME()) + COLON,
                                               COMMA if (ctx.roles()) else CLOSE_BRACE)
        self.game.players.list.append(player)

    # Enter a parse tree produced by dgdlParser#roles.
    def enterRoles(self, ctx: dgdlParser.RolesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principles.
    def enterPrinciples(self, ctx: dgdlParser.PrinciplesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principle.
    def enterPrinciple(self, ctx: dgdlParser.PrincipleContext):
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

    def create_game(self, input_stream):
        lexer = dgdlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = dgdlParser(stream)
        tree = parser.game()
        listener = GameFactory()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
