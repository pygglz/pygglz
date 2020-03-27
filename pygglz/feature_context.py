from copy import copy

from .context_locator import ContextLocator
from .feature_state import FeatureState
from .state_repository import StateRepository


class FeatureContext(object):
    def __init__(self, state_repository: StateRepository,
                 context_locator: ContextLocator = None,
                 read_only: bool = True):
        self.feature_states = {}
        self.state_repository = state_repository
        self.context_locator = context_locator
        self.read_only = read_only
        self.load_feature_states()

    def __getitem__(self, item):
        return self.is_feature_active(item)

    def is_feature_active(self, name):
        feature_state = self.get_feature_state(name)
        return feature_state is not None and feature_state.enabled

    def load_feature_states(self):
        features_states = self.state_repository.get_feature_states()
        for key, value in features_states.items():
            if not key in self.feature_states:
                self.feature_states[key] = value

    def get_feature_names(self):
        return [k for k in self.feature_states.keys()]

    def get_feature_state(self, name: str) -> FeatureState:
        feature_state = self.feature_states.get(name, None) \
                        or self.state_repository.get_feature_state(name)
        if feature_state is not None:
            self.feature_states[name] = feature_state
        return copy(feature_state)

    def set_feature_state(self, feature_state: FeatureState) -> None:
        if self.read_only:
            raise RuntimeError("Feature context is read only.")

        self.feature_states[feature_state.name] = copy(feature_state)
        self.state_repository.set_feature_state(feature_state)

    def __enter__(self) -> 'FeatureContext':
        self.context_locator.push_context(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.context_locator.pop_context()
