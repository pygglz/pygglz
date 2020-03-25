from .context_locator import ContextLocator
from .feature_context import FeatureContext
from .features import Features
from .state_repository import StateRepository

_global_state_repository = StateRepository()
_global_context = FeatureContext(_global_state_repository)
_context_locator = ContextLocator(_global_context)

features = Features(_context_locator)


def configure(state_repository: StateRepository = None):
    if state_repository:
        _global_context.state_repository = state_repository
