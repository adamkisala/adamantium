class Content:
    def __init__(self):
        self._list = []

    def _get_list(self) -> []:
        return self._list

    def _set_list(self, list_tmp: [] = None):
        self._list = list_tmp

    list = property(_get_list, _set_list, None)
