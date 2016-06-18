from enums.Structure import Structure
from enums.Visibility import Visibility


class Store:
    def __init__(self):
        self._structure = None
        self._visibility = None
        self._name = None
        self._owner = []

    def _set_structure(self, structure_tmp: Structure = None):
        if structure_tmp == str.lower(Structure.SET.name):
            self._structure = Structure.SET
        elif structure_tmp == str.lower(Structure.QUEUE.name):
            self._structure = Structure.QUEUE
        elif structure_tmp == str.lower(Structure.STACK.name):
            self._structure = Structure.STACK

    def _get_structure(self) -> Structure:
        return self._structure

    def _set_visibility(self, visibility_tmp: Visibility = None):
        if visibility_tmp == str.lower(Visibility.PRIVATE.name):
            self._visibility = Visibility.PRIVATE
        elif visibility_tmp == str.lower(Visibility.PUBLIC.name):
            self._visibility = Visibility.PUBLIC

    def _get_visibility(self) -> Visibility:
        return self._visibility

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _get_name(self) -> str:
        return self._name

    def _set_owner(self, owner_tmp: [] = None):
        self._owner = owner_tmp

    def _get_owner(self) -> []:
        return self._owner

    structure = property(_get_structure, _set_structure)
    visibility = property(_get_visibility, _set_visibility)
    name = property(_get_name, _set_name)
    owner = property(_get_owner, _set_owner)
