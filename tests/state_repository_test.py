import unittest

from pygglz.feature_state import FeatureState
from pygglz.state_repository import StateRepository


class TestRepo(StateRepository):
    def __init__(self):
        self.loaded = False
        super().__init__()

    def load(self) -> dict:
        self.loaded = True
        return super().load()


class StateRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = TestRepo()

    def test_not_loaded_on_creation(self):
        self.assertFalse(self.repo.loaded)

    def test_load_called_on_get_feature_state(self):
        self.repo.get_feature_state("A")

        self.assertTrue(self.repo.loaded)

    def test_load_called_on_set_feature_state(self):
        self.repo.set_feature_state(FeatureState("A", enabled=True))

        self.assertTrue(self.repo.loaded)

    def test_load_called_on_get_feature_states(self):
        self.repo.get_feature_states()

        self.assertTrue(self.repo.loaded)

    def test_load_called_on_get_feature_names(self):
        self.repo.get_feature_names()

        self.assertTrue(self.repo.loaded)
