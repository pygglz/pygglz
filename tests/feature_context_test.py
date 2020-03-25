import unittest

from mockito import mock, when

from togglz.feature_context import FeatureContext


class FeatureContextTest(unittest.TestCase):
    def test_delegates_to_manager(self):
        self.__given_a_context_with_feature_manager({"ENABLED": True, "DISABLED": False})

        self.assertTrue(self.context.ENABLED)
        self.assertFalse(self.context.DISABLED)
        self.assertFalse(self.context.NON_EXISTENT)

    def __given_a_context_with_feature_manager(self, features):
        feature_manager = mock()
        for k, v in features.items():
            feature = mock()
            feature.name = k
            feature.enabled = v
            when(feature_manager).get_feature(k).thenReturn(feature)
        self.context = FeatureContext(feature_manager=feature_manager)