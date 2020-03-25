from typing import Optional

from .feature_state import FeatureState
from .state_repository import StateRepository


class FeatureManager(object):
    def __init__(self, state_repository: StateRepository):
        self._feature_states = state_repository.get_feature_states()

    def get_feature_state(self, name: str) -> Optional[FeatureState]:
        return self._feature_states.get(name, None)
