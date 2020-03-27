from copy import copy

from .feature_state import FeatureState


class StateRepository(object):
    def __init__(self):
        self.feature_states = {}

    def get_feature_states(self) -> dict:
        return self.feature_states

    def get_feature_state(self, name: str) -> FeatureState:
        feature_state = self.feature_states.get(name)
        return copy(feature_state) or FeatureState(name, False)

    def set_feature_state(self, feature_state: FeatureState) -> None:
        self.feature_states[feature_state.name] = copy(feature_state)
