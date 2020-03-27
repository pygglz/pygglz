from copy import copy
from copy import deepcopy

from .feature_state import FeatureState


class StateRepository(object):
    def __init__(self):
        self.feature_states = self.load()

    def load(self) -> dict:
        """to be implemented"""
        return {}

    def save(self, feature_state: FeatureState):
        """to be implemented"""
        pass

    def get_feature_names(self):
        return [k for k in self.feature_states.keys()]

    def get_feature_states(self) -> dict:
        return deepcopy(self.feature_states)

    def get_feature_state(self, name: str) -> FeatureState:
        feature_state = self.feature_states.get(name, None)
        return copy(feature_state)

    def set_feature_state(self, feature_state: FeatureState) -> None:
        self.feature_states[feature_state.name] = copy(feature_state)
        self.save(feature_state)
