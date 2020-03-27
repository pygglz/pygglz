import json
import unittest
from tempfile import mktemp

from pygglz.feature_state import FeatureState
from pygglz.file_repository import FileRepository


class FileRepositoryTest(unittest.TestCase):
    def test_loads_if_file_not_exists(self):
        filename = mktemp(".json")
        repo = FileRepository(filename)
        self.assertEqual([], [k for k, v in repo.get_feature_states().items()])

    def test_loads_if_file_exists(self):
        filename = mktemp(".json")
        with open(filename, 'w') as file:
            json.dump({"FLAG": {"enabled": True}}, file)
        repo = FileRepository(filename)
        self.assertEqual(["FLAG"], [k for k, v in repo.get_feature_states().items()])
        self.assertTrue(repo.get_feature_state("FLAG").enabled)

    def test_saves_on_change(self):
        filename = mktemp(".json")
        repo = FileRepository(filename)
        repo.set_feature_state(FeatureState("FLAG", True))

        with open(filename, "r") as file:
            data = json.load(file)
        self.assertTrue(data["FLAG"]["enabled"])
