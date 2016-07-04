from interface.IHandler import IHandler
from enums.Scope import Scope
from enums.HandlerType import HandlerType
from model.GameStatus import GameStatus
from helpers.Constants import *


class RulesController(IHandler):
    def update_collector(self, game_status_tmp: GameStatus = None):
        return game_status_tmp

    def update_flag(self):
        pass

    def type(self):
        return HandlerType.PRE_MOVE_CHECK

    def __init__(self):
        super().__init__()

    def handle(self, game_status_tmp: GameStatus = None):
        principles = self.__get_principles_to_update(game_status_tmp)
        self.__evaluate_principle(principles)
        game_status_tmp = self.update_collector(game_status_tmp)
        self.update_flag()
        if DEBUG:
            print("Handling in: " + str(type(self)))
        return game_status_tmp

    def __get_principles_to_update(self, game_status_tmp: GameStatus = None) -> []:
        values = []
        for principle in game_status_tmp.principles:
            if principle.scope == Scope.MOVEWISE:
                if DEBUG:
                    print("Evaluating: " + str(principle))
                values.append(principle)
            elif principle.scope == Scope.TURNWISE and game_status_tmp.new_turn:
                if DEBUG:
                    print("Evaluating: " + str(principle))
                values.append(principle)
            elif principle.scope == Scope.INITIAL and game_status_tmp.initial_turn:
                if DEBUG:
                    print("Evaluating: " + str(principle))
                values.append(principle)
            else:
                if DEBUG:
                    print("Not evaluating: " + str(principle))
        return values

    def __evaluate_principle(self, principles_tmp: [] = None):
        for principle in principles_tmp:
            if DEBUG:
                print("Checking conditions of: " + str(principle))
            # TODO check condition here and apply effects
