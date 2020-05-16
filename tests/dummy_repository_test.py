import unittest

from pygglz.dummy_repository import DummyRepository
from pygglz.feature_state import FeatureState


class DummyRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = DummyRepository()

    def test_enabled_after_set(self):
        self.assertIsNone(self.repo.get_feature_state("A"))

        self.repo.set_feature_state(FeatureState("A", enabled=True))

        self.assertTrue(self.repo.get_feature_state("A").enabled)
