import unittest

from mockito import mock, when

from togglz.feature_manager import FeatureManager
from togglz.feature_state import FeatureState


class FeatureManagerTest(unittest.TestCase):
    def test_delegates_to_manager(self):
        self.__given_a_manager_with_repo({"ENABLED": True, "DISABLED": False})

        self.assertTrue(self.manager.get_feature_state("ENABLED").enabled)
        self.assertFalse(self.manager.get_feature_state("DISABLED").enabled)
        self.assertIsNone(self.manager.get_feature_state("NON_EXISTENT"))

    def __given_a_manager_with_repo(self, features):
        self.repo = mock()
        when(self.repo).load_features().thenReturn({k: FeatureState(name=k, enabled=v) for k, v in features.items()})
        self.manager = FeatureManager(repository=self.repo)
