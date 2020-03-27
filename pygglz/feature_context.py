from copy import copy

from .context_locator import ContextLocator
from .feature_snapshot import FeatureSnapshot
from .feature_state import FeatureState
from .state_repository import StateRepository


class FeatureContext(object):
    def __init__(self, state_repository: StateRepository,
                 context_locator: ContextLocator = None,
                 snapshot: bool = True,
                 read_only: bool = True):
        self.read_only = read_only
        self.state_repository = state_repository
        self.context_locator = context_locator
        self.configure(state_repository, snapshot, read_only)

    def configure(self, state_repository: StateRepository,
                  snapshot: bool = True,
                  read_only: bool = True):
        self.read_only = read_only
        self.state_repository = state_repository
        if snapshot:
            self.feature_states = FeatureSnapshot(state_repository)
        else:
            self.feature_states = state_repository

    def __getitem__(self, item):
        return self.is_feature_active(item)

    def is_feature_active(self, name):
        feature_state = self.get_feature_state(name)
        return feature_state is not None and feature_state.enabled

    def get_feature_names(self) -> list:
        return self.feature_states.get_feature_names()

    def get_feature_state(self, name: str) -> FeatureState:
        feature_state = self.feature_states.get_feature_state(name)
        return copy(feature_state)

    def set_feature_state(self, feature_state: FeatureState) -> None:
        if self.read_only:
            raise RuntimeError("Feature context is read only.")
        self.feature_states.set_feature_state(copy(feature_state))

    def __enter__(self) -> 'FeatureContext':
        self.context_locator.push_context(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.context_locator.pop_context()
