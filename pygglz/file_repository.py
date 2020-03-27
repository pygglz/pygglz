import json
from os import path

from .feature_state import FeatureState
from .state_repository import StateRepository


class FileRepository(StateRepository):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    def load(self):
        if not path.isfile(self.filename):
            return {}

        with open(self.filename, 'r') as file:
            data: dict = json.load(file)
            return {k: FeatureState(k, v["enabled"]) for k, v in data.items()}

    def save(self, feature_state):
        data = self.load()
        data[feature_state.name] = {"enabled": feature_state.enabled}
        with open(self.filename, 'w') as file:
            json.dump(data, file)
