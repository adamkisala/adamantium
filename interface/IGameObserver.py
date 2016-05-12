from abc import ABCMeta, abstractmethod
from engine.interface import IGameDataCollector


class IGameObserver(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self, iGameDataCollector):
        """

        :type iGameDataCollector: IGameDataCollector
        """
        pass
