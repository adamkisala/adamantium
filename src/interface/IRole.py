from abc import ABCMeta, abstractmethod


class IRole(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
