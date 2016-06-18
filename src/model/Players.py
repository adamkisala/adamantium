class Players:
    def __init__(self):
        self._min = None
        self._max = None
        self._list = []

    def _set_min(self, min_tmp: int = None):
        self._min = min_tmp

    def _get_min(self) -> int:
        return self._min

    def _set_max(self, max_tmp: int = None):
        self._max = max_tmp

    def _get_max(self) -> int:
        return self._max

    def _set_list(self, list_tmp: [] = None):
        self._list = list_tmp

    def _get_list(self) -> []:
        return self._list

    min = property(_get_min, _set_min, None)
    max = property(_get_max, _set_max, None)
    list = property(_get_list, _set_list, None)
