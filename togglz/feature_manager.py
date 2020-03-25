from typing import Optional

from .feature_repository import FeatureRepository
from .feature_state import FeatureState


class FeatureManager(object):
    def __init__(self, repository: FeatureRepository):
        self._feature_states = repository.load_features()

    def get_feature_state(self, name: str) -> Optional[FeatureState]:
        return self._feature_states.get(name, None)
