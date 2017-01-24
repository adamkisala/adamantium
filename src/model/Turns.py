from enums.Magnitude import *
from enums.Ordering import *


# TODO !!! max is NULL you bum! where it doesn't have to be defined in the description
class Turns:
    def __init__(self):
        self.__magnitude = None
        self.__ordering = None
        self.__max = None

    def __set_magnitude(self, magnitude_tmp: Magnitude = None):
        if magnitude_tmp == str.lower(Magnitude.SINGLE.name):
            self._magnitude = Magnitude.SINGLE
        elif magnitude_tmp == str.lower(Magnitude.MULTIPLE.name):
            self._magnitude = Magnitude.MULTIPLE

    def __set_ordering(self, ordering_tmp: Ordering = None):
        if ordering_tmp == str.lower(Ordering.LIBERAL.name):
            self._ordering = Ordering.LIBERAL
        elif ordering_tmp == str.lower(Ordering.STRICT.name):
            self._ordering = Ordering.STRICT

    def __set_max(self, max_tmp: int = None):
        self._max = max_tmp

    def __get_magnitude(self) -> Magnitude:
        return self._magnitude

    def __get_ordering(self) -> Ordering:
        return self._ordering

    def __get_max(self) -> int:
        return self._max

    ordering = property(__get_ordering, __set_ordering, None)
    magnitude = property(__get_magnitude, __set_magnitude, None)
    max = property(__get_max, __set_max, None)
