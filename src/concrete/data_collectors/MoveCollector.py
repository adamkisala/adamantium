from concrete.ConsoleInputController import ConsoleInputController
from interface.IGameDataCollector import IGameDataCollector


class MoveCollector(IGameDataCollector):
    def collect(self):
        self.__console_input_controller.get_input()

    def __init__(self):
        super().__init__()
        self.__console_input_controller = ConsoleInputController()
