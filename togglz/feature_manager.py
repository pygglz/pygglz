from .feature_repository import FeatureRepository
from .feature import Feature

class FeatureManager(object):
    def __init__(self, repository: FeatureRepository):
        self._features = repository.load_features()

    def get_feature(self, name: str) -> Feature:
        return self._features.get(name, None)
