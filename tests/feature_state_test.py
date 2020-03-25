import unittest

from togglz.feature_state import FeatureState


class FeatureTest(unittest.TestCase):
    def test_init(self):
        f = FeatureState("Enabled", True)

        self.assertEqual("Enabled", f.name)
        self.assertTrue(f.enabled)
