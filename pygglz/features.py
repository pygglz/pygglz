from .context_locator import ContextLocator
from .feature_context import FeatureContext
from .feature_state import FeatureState


class Features(object):
    def __init__(self, context_locator: ContextLocator):
        self.context_locator = context_locator

    def __getitem__(self, item) -> bool:
        return self.get_feature_state(item).enabled

    def get_feature_state(self, name: str) -> FeatureState:
        return self.context_locator.peek_context().get_feature_state(name)

    def new_feature_context(self):
        feature_context = self.context_locator.peek_context()
        return FeatureContext(feature_context.state_repository, self.context_locator)
