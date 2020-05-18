import unittest

from pygglz.feature_state import FeatureState


class FeatureStateTest(unittest.TestCase):
    def test_init(self):
        f = FeatureState("Enabled", True)

        self.assertEqual("Enabled", f.name)
        self.assertTrue(f.enabled)

    def test_eq_if_attributes_match(self):
        a_enabled = FeatureState("a", enabled=True)
        self.assertEqual(FeatureState("a", enabled=True), a_enabled)

    def test_ne_if_name_doesnt_match(self):
        a = FeatureState("a", enabled=True)
        self.assertNotEqual(FeatureState("b", enabled=True), a)

    def test_ne_if_enabled_doesnt_match(self):
        a = FeatureState("a", enabled=True)
        self.assertNotEqual(FeatureState("a", enabled=False), a)

    def test_repr(self):
        a = FeatureState("a", enabled=True)
        self.assertEqual("<FeatureState name=a enabled=True>", repr(a))
