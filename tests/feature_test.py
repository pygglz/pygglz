import unittest

from togglz.feature import Feature


class FeatureTest(unittest.TestCase):
    def test_init(self):
        f = Feature("Enabled", True)

        self.assertEqual("Enabled", f.name)
        self.assertTrue(f.enabled)
