import unittest

from pygglz.feature_state import FeatureState
from pygglz.memory import MemoryRepository


class MemoryRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = MemoryRepository()

    def test_get_enabled_feature_state(self):
        self.repo.feature_states = {"A": FeatureState("A", enabled=True)}

        feature_state = self.repo.get_feature_state("A")

        self.assertTrue(feature_state.enabled)

    def test_get_disabled_feature_state(self):
        self.repo.feature_states = {"A": FeatureState("A", enabled=False)}

        feature_state = self.repo.get_feature_state("A")

        self.assertFalse(feature_state.enabled)

    def test_get_non_existent_feature_state(self):
        self.repo.feature_states = {}

        feature_state = self.repo.get_feature_state("A")

        self.assertIsNone(feature_state)

    def test_set_non_feature_state(self):
        self.repo.set_feature_state(FeatureState("A", enabled=True))

        self.assertEqual(self.repo.feature_states, {"A": FeatureState("A", enabled=True)})
