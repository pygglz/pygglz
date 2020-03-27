from .feature_state import FeatureState
from .state_repository import StateRepository


class FeatureSnapshot(object):
    def __init__(self, state_repository: StateRepository):
        self.state_repository = state_repository
        self.feature_states = self.state_repository.get_feature_states()

    def get_feature_names(self) -> list:
        return [k for k in self.feature_states.keys()]

    def get_feature_state(self, name: str) -> FeatureState:
        feature_state = self.feature_states.get(name, None) \
                        or self.state_repository.get_feature_state(name)
        if feature_state:
            self.feature_states[name] = feature_state
        return feature_state

    def set_feature_state(self, feature_state: FeatureState) -> None:
        self.state_repository.set_feature_state(feature_state)
        self.feature_states[feature_state.name] = feature_state
