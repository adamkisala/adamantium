from abc import ABCMeta, abstractmethod


class Role(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
