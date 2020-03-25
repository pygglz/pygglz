from .feature import Feature
from .feature_manager import FeatureManager
from .feature_repository import FeatureRepository


class FeatureContext(object):
    def __init__(self, feature_manager: FeatureManager = None):
        self.feature_manager = feature_manager or FeatureManager(repository=FeatureRepository())

    def configure(self, feature_manager: FeatureManager = None):
        if feature_manager is not None:
            self.feature_manager = feature_manager

    def __getattr__(self, item):
        return self.is_feature_enabled(item)

    def is_feature_enabled(self, name: str):
        feature = self.feature_manager.get_feature(name)
        if feature is None:
            return False
        return feature.enabled

    def get_feature(self, name: str):
        feature = self.feature_manager.get_feature(name)
        return feature or Feature(name, False)
