from enums.Magnitude import *
from enums.Ordering import *


class Turns:
    def __init__(self):
        self._magnitude = None
        self._ordering = None
        self._max = None

    def _set_magnitude(self, magnitude_tmp: Magnitude = None):
        self._magnitude = magnitude_tmp

    def _set_ordering(self, ordering_tmp: Ordering = None):
        self._ordering = ordering_tmp

    def _set_max(self, max_tmp: int = None):
        self._max = max_tmp

    def _get_magnitude(self) -> Magnitude:
        return self._magnitude

    def _get_ordering(self) -> Ordering:
        return self._ordering

    def _get_max(self) -> int:
        return self._max

    ordering = property(_get_ordering, _set_ordering, None)
    magnitude = property(_get_magnitude, _set_magnitude, None)
    max = property(_get_max, _set_max, None)
