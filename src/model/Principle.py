from enums.Scope import Scope
from model.Condition import Condition
from model.Effect import Effect


class Principle:
    def __init__(self):
        self._name = None
        self._scope = Scope
        self._effect = Effect()
        self._condition = Condition()

    def _get_name(self) -> str:
        return self._name

    def _set_name(self, name_tmp: str = None):
        self._name = name_tmp

    def _set_scope(self, scope_tmp: Scope = None):
        self._scope = scope_tmp

    def _get_scope(self) -> Scope:
        return self._scope

    def _set_effect(self, effect_tmp: Effect = None):
        self._effect = effect_tmp

    def _get_effect(self) -> Effect:
        return self._effect

    def _set_condition(self, condition_tmp: Condition = None):
        self._condition = condition_tmp

    def _get_condition(self) -> Condition:
        return self._condition

    name = property(_get_name, _set_name, None)
    scope = property(_get_scope, _set_scope, None)
    effect = property(_get_effect, _set_effect, None)
    condition = property(_get_condition, _set_condition, None)