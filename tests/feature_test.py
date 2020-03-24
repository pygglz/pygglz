import unittest

from togglz.feature import Feature


class FeatureTest(unittest.TestCase):
    def test_new_enabled(self):
        f = Feature("Enabled", True)

        self.assertEqual("Enabled", f.name)
        self.assertTrue(f.enabled)

    def test_new_disabled(self):
        f = Feature("Disabled", False)

        self.assertEqual("Disabled", f.name)
        self.assertFalse(f.enabled)
