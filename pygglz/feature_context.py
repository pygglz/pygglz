from .context_locator import ContextLocator
from .feature_state import FeatureState
from .state_repository import StateRepository


class FeatureContext(object):
    def __init__(self, state_repository: StateRepository, context_locator: ContextLocator = None):
        self.state_repository = state_repository
        self.context_locator = context_locator
        self._feature_states = state_repository.get_feature_states()

    def __getitem__(self, item):
        return self.get_feature_state(item).enabled

    def get_feature_state(self, name: str) -> FeatureState:
        return self._feature_states.get(name, None) \
               or self.state_repository.get_feature_state(name) \
               or FeatureState(name, False)

    def __enter__(self):
        self.context_locator.push_context(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context_locator.pop_context()
