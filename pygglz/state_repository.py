from .feature_state import FeatureState


class StateRepository(object):
    def get_feature_states(self):
        return {}

    def get_feature_state(self, name: str) -> FeatureState:
        return FeatureState(name, False)
