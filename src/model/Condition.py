class Condition:
    def __init__(self):
        self._name = None
        self._list = []

    def _get_name(self) -> str:
        return self._name

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _get_list(self) -> []:
        return self._list

    def _set_list(self, list_tmp: [] = None):
        self._list = list_tmp

    name = property(_get_name, _set_name, None)
    list = property(_get_list, _set_list, None)