from copy import copy

from .context_locator import ContextLocator
from .feature_state import FeatureState
from .state_repository import StateRepository


class FeatureContext(object):
    def __init__(self, state_repository: StateRepository,
                 context_locator: ContextLocator = None,
                 cache_state: bool = True,
                 read_only: bool = None):
        self.feature_states = {}
        self.state_repository = state_repository
        self.context_locator = context_locator
        self.cache_state = cache_state
        self.read_only = read_only is not False
        self.load_feature_states()

    def __getitem__(self, item):
        return self.is_feature_active(item)

    def is_feature_active(self, name):
        return self.get_feature_state(name).enabled

    def load_feature_states(self):
        if not self.cache_state:
            return

        features_states = self.state_repository.get_feature_states()
        for key, value in features_states.items():
            if not key in self.feature_states:
                self.feature_states[key] = copy(value)

    def get_feature_state(self, name: str) -> FeatureState:
        return copy(self.feature_states.get(name, None)) \
               or copy(self.state_repository.get_feature_state(name)) \
               or FeatureState(name, False)

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
