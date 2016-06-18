
class Player:
    def __init__(self):
        self._name = None
        self._roles = []

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _get_name(self) -> str:
        return self._name

    def _set_roles(self, roles_tmp: [] = None):
        self._roles = roles_tmp

    def _get_roles(self) -> []:
        return self._roles

    name = property(_get_name, _set_name, None)
    roles = property(_get_roles, _set_roles, None)

