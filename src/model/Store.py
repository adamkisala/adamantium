from enums import Structure, Visibility


class Store:
    def __init__(self):
        self._structure = None
        self._visibility = None
        self._name = None
        self._owner = []

    def set_structure(self, structure_tmp: Structure = None):
        self._structure = structure_tmp

    def get_structure(self) -> Structure:
        return self._structure

    def set_visibility(self, visibility_tmp: Visibility = None):
        self._visibility = visibility_tmp

    def get_visibility(self) -> Visibility:
        return self._visibility

    def set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def get_name(self) -> str:
        return self._name

    def set_owner(self, owner_tmp: [] = None):
        self._owner = owner_tmp

    def get_owner(self) -> []:
        return self._owner

    structure = property(get_structure, set_structure)
    visibility = property(get_visibility, set_visibility)
    name = property(get_name, set_name)
    owner = property(get_owner, set_owner)
