import json

import requests

from .feature_state import FeatureState
from .state_repository import StateRepository


class HttpRepository(StateRepository):
    def __init__(self, url):
        self.url = url
        super().__init__()

    def load(self):
        response = requests.get(self.url, headers={"Accept": "application/json"})
        if not response.ok:
            response.raise_for_status()

        json_doc = json.loads(response.content)
        return {k: FeatureState(k, v["enabled"]) for k, v in json_doc.items()}

    def save(self, feature_state):
        data = {k: {"enabled": v.enabled} for k, v in self.feature_states.items()}
        response = requests.put(self.url, data=data)
        if not response.ok:
            response.raise_for_status()
