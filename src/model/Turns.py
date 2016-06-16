class Turns:
    def __init__(self):
        self._magnitude = None
        self._ordering = None

    def set_magnitude(self, magnit=None):
        self._magnitude = magnit

    def set_ordering(self, ord=None):
        self._ordering = ord

    def get_magnitude(self):
        return self._magnitude

    def get_ordering(self):
        return self._ordering

    def commit(self):
        pass

    ordering = property(get_ordering, set_ordering)
    magnitude = property(get_magnitude, set_magnitude)
