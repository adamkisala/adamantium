from model.Content import Content


class Move:
    def __init__(self):
        self._name = None
        self._content = Content()
        self._effects = []
        self._condition = []
        self.__final = False

    def _get_name(self) -> str:
        return self._name

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _set_content(self, content_tmp: Content = None):
        self._content = content_tmp

    def _get_content(self) -> Content:
        return self._content

    def _set_effect(self, effects_tmp: [] = None):
        self._effects = effects_tmp

    def _get_effect(self) -> []:
        return self._effects

    def _set_condition(self, condition_tmp: [] = None):
        self._condition = condition_tmp

    def _get_condition(self) -> []:
        return self._condition

    def __get_final(self) -> bool:
        return self.__final

    def __set_final(self, final_tmp: bool = False):
        self.__final = final_tmp

    id = property(_get_name, _set_name, None)
    effects = property(_get_effect, _set_effect, None)
    conditions = property(_get_condition, _set_condition, None)
    content = property(_get_content, _set_content, None)
    final = property(__get_final, __set_final, None)
