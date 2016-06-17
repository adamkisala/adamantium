from enums.Magnitude import *
from enums.Ordering import *


class Turns:
    def __init__(self):
        self._magnitude = None
        self._ordering = None

    def set_magnitude(self, magnitude_tmp: Magnitude = None):
        """

        :param magnitude_tmp:
        """
        self._magnitude = magnitude_tmp

    def set_ordering(self, ordering_tmp: Ordering = None):
        self._ordering = ordering_tmp

    def get_magnitude(self) -> Magnitude:
        return self._magnitude

    def get_ordering(self) -> Ordering:
        return self._ordering

    def commit(self):
        pass

    ordering = property(get_ordering, set_ordering, None)
    magnitude = property(get_magnitude, set_magnitude, None)
