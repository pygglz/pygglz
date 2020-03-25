from .context_locator import ContextLocator
from .feature_state import FeatureState


class Features(object):
    def __init__(self, locator: ContextLocator):
        self._locator = locator

    def __getitem__(self, item) -> bool:
        return self.get_feature_state(item).enabled

    def get_feature_state(self, name: str) -> FeatureState:
        return self._locator.peek_context().get_feature_state(name)
