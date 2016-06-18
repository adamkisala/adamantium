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
from gen.dgdlVisitor import *
from model.Principle import *

class GameFactory(dgdlListener, dgdlVisitor):
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
        if ctx.roles():
            roles = self.visit(ctx.roles())
            player.roles = roles
        self.game.players.list.append(player)

    # Enter a parse tree produced by dgdlParser#roles.
    def enterRoles(self, ctx: dgdlParser.RolesContext):
        if (ctx.getRuleContext() == self.exitStore) or (ctx.getRuleIndex() == self.exitPlayer):
            roles = self.visit(dgdlParser.RolesContext)
            self.game.roles = roles

    # Enter a parse tree produced by dgdlParser#principles.
    def enterPrinciples(self, ctx: dgdlParser.PrinciplesContext):
        pass

    # Enter a parse tree produced by dgdlParser#principle.
    def enterPrinciple(self, ctx: dgdlParser.PrincipleContext):
        principle = Principle()
        data = str(ctx.getText())
        if str(ctx.IDENT()) in data:
            principle.name = StringParser.before(data, OPEN_BRACE)
        if ctx.scope():
            principle.scope = self.visit(ctx.scope())
        if ctx.conditions():
            principle.conditions = self.visit(ctx.conditions())
        if ctx.effects():
            principle.effects = self.visit(ctx.effects())

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

    # Visit a parse tree produced by dgdlParser#roles.
    def visitRoles(self, ctx: dgdlParser.RolesContext):
        data = str(ctx.getText())
        values = []
        if str(ctx.ROLES()) in data:
            roles = StringParser.between(data, str(ctx.ROLES()) + OPEN_BRACE, CLOSE_BRACE)
            values = roles.split(",")
        return values

    # Visit a parse tree produced by dgdlParser#scope.
    def visitScope(self, ctx: dgdlParser.ScopeContext):
        data = str(ctx.getText())
        scope = None
        if str(ctx.SCOPE()) in data:
            scope = StringParser.after(data, str(ctx.SCOPE()) + COLON)
        return scope

    # Visit a parse tree produced by dgdlParser#conditions.
    def visitConditions(self, ctx:dgdlParser.ConditionsContext):
        data = str(ctx.getText())
        condition = Condition()
        values = []
        if str(ctx.CONDITIONS()) in data:
            condition.name = StringParser.before(data, OPEN_BRACE)
            conditions = StringParser.between(data, str(ctx.CONDITIONS()) + OPEN_BRACE, CLOSE_BRACE)
            condition.list = conditions.split(",")
        return condition

    # Visit a parse tree produced by dgdlParser#effects.
    def visitEffects(self, ctx: dgdlParser.EffectsContext):
        data = str(ctx.getText())
        effect = Effect()
        values = []
        if str(ctx.EFFECTS()) in data:
            effect.name = StringParser.before(data, OPEN_BRACE)
            effects = StringParser.between(data, str(ctx.EFFECTS()) + OPEN_BRACE, CLOSE_BRACE)
            effect.list = effects.split(",")
        return effect

    def create_game(self, input_stream):
        lexer = dgdlLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = dgdlParser(stream)
        tree = parser.game()
        listener = GameFactory()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
