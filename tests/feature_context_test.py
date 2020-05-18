import unittest

from mockito import mock, when

from pygglz.feature_context import FeatureContext
from pygglz.state_repository import StateRepository


class FeatureContextTest(unittest.TestCase):
    def test_delegates_to_manager(self):
        self.__given_a_context_with_state_repo({"ENABLED": True, "DISABLED": False})

        self.assertTrue(self.context["ENABLED"])
        self.assertFalse(self.context["DISABLED"])
        self.assertFalse(self.context["NON_EXISTENT"])

    def __given_a_context_with_state_repo(self, features):
        state_repository = mock()
        for k, v in features.items():
            feature_state = mock({"name": k, "enabled": v})
            when(state_repository).get_feature_state(k).thenReturn(feature_state)
        when(state_repository).get_feature_states().thenReturn({})
        self.context = FeatureContext(state_repository)

    def test_enabled_disabled_features_on_configure(self):
        self.context = FeatureContext(state_repository=StateRepository(),
                                      enabled_features=["A", "B"],
                                      disabled_features=["B", "C"])
        self.assertTrue(self.context.is_feature_active("A"))
        self.assertFalse(self.context.is_feature_active("B"))
        self.assertFalse(self.context.is_feature_active("C"))
        self.assertFalse(self.context.is_feature_active("D"))

    def test_enabled_features_on_configure(self):
        self.context = FeatureContext(state_repository=StateRepository(),
                                      enabled_features=["A", "B"])
        self.assertTrue(self.context.is_feature_active("A"))
        self.assertTrue(self.context.is_feature_active("B"))

    def test_disabled_features_on_configure(self):
        self.context = FeatureContext(state_repository=StateRepository(),
                                      disabled_features=["A", "B"])
        self.assertFalse(self.context.is_feature_active("A"))
        self.assertFalse(self.context.is_feature_active("B"))
        self.assertFalse(self.context.is_feature_active("C"))
