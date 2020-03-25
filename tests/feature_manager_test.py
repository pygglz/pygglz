import unittest

from mockito import mock, when

from togglz.feature import Feature
from togglz.feature_manager import FeatureManager


class FeatureManagerTest(unittest.TestCase):
    def test_delegates_to_manager(self):
        self.__given_a_manager_with_repo({"ENABLED": True, "DISABLED": False})

        self.assertTrue(self.manager.get_feature("ENABLED").enabled)
        self.assertFalse(self.manager.get_feature("DISABLED").enabled)
        self.assertIsNone(self.manager.get_feature("NON_EXISTENT"))

    def __given_a_manager_with_repo(self, features):
        self.repo = mock()
        when(self.repo).load_features().thenReturn({k: Feature(name=k, enabled=v) for k, v in features.items()})
        self.manager = FeatureManager(repository=self.repo)
