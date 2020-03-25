from .feature_context import FeatureContext
from .feature_manager import FeatureManager

_root_context = FeatureContext()

features = _root_context

configure = _root_context.configure
