import json
import unittest
from tempfile import mktemp

from pygglz.feature_state import FeatureState
from pygglz.features import Features
from pygglz.file_repository import FileRepository


class FeaturesFileIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.features = Features()

    def test_sub_context_is_isolated(self):
        filename = mktemp(".json")
        file_repo = FileRepository(filename)
        self.features.configure(state_repository=file_repo)

        with self.features.new_feature_context(read_only=False):
            self.features.set_feature_state(FeatureState("FLAG", True))

            with open(filename, 'r') as file:
                data = json.load(file)
            self.assertTrue(data["FLAG"]["enabled"])
