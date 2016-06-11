from abc import ABCMeta, abstractmethod


class Observable(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def notify_all(self):
        pass
