import unittest

from mockito import mock, when, verify

from pygglz.feature_snapshot import FeatureSnapshot
from pygglz.feature_state import FeatureState


class FeatureSnapshotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.state_repo = mock()

    def test_pass_through_to_repo_if_missing(self):
        self.__given_repo_with_feature_enabled("F1")
        self.__given_snapshot({})

        feature_state = self.snapshot.get_feature_state("F1")
        self.assertTrue(feature_state.enabled)

    def test_dont_pass_through_to_repo_if_present(self):
        self.__given_snapshot({"F1": FeatureState("F1", True)})

        feature_state = self.snapshot.get_feature_state("F1")
        self.assertTrue(feature_state.enabled)
        verify(self.state_repo, times=0).get_feature_state("F1")

    def __given_repo_with_feature_enabled(self, feature_name):
        feature_state = FeatureState(feature_name, True)
        when(self.state_repo).get_feature_state(feature_name).thenReturn(feature_state)

    def __given_snapshot(self, feature_states=None):
        when(self.state_repo).get_feature_states().thenReturn(feature_states or {})
        self.snapshot = FeatureSnapshot(self.state_repo)
