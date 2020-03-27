from .context_locator import ContextLocator
from .feature_context import FeatureContext
from .feature_state import FeatureState
from .state_repository import StateRepository


class Features(object):
    def __init__(self):
        self.global_context = FeatureContext(StateRepository(), None,
                                             snapshot=False,
                                             read_only=False)
        self.context_locator = ContextLocator(self.global_context)

    def configure(self, state_repository: StateRepository = None,
                  snapshot=False, read_only=False):
        self.global_context.configure(state_repository=state_repository,
                                      snapshot=snapshot,
                                      read_only=read_only)

    def __getitem__(self, item) -> bool:
        return self.is_feature_active(item)

    def get_feature_names(self):
        return self.context_locator.peek_context().get_feature_names()

    def set_feature_enabled(self, name: str, enabled: bool = True):
        feature_state = self.get_feature_state(name) or FeatureState(name, enabled)
        feature_state.enabled = enabled
        self.set_feature_state(feature_state)

    def is_feature_active(self, name: str) -> bool:
        return self.context_locator.peek_context().is_feature_active(name)

    def get_feature_state(self, name: str) -> FeatureState:
        return self.context_locator.peek_context().get_feature_state(name)

    def set_feature_state(self, feature_state: FeatureState):
        return self.context_locator.peek_context().set_feature_state(feature_state)

    def new_feature_context(self, state_repository: StateRepository = None,
                            read_only: bool = True,
                            snapshot: bool = True):
        feature_context = self.context_locator.peek_context()
        return FeatureContext(state_repository or feature_context.state_repository,
                              self.context_locator,
                              snapshot=snapshot,
                              read_only=read_only)
