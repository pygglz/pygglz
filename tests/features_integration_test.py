import unittest

from pygglz.features import Features


class FeaturesTest(unittest.TestCase):
    def setUp(self) -> None:
        self.features = Features()

    def test_sub_context_is_isolated(self):
        self.assertNotIn("FLAG", self.features.get_feature_names())

        with self.features.new_feature_context(read_only=False):
            self.assertNotIn("FLAG", self.features.get_feature_names())
            self.assertFalse(self.features["FLAG"])
            self.features.set_feature_enabled("FLAG")
            self.assertIn("FLAG", self.features.get_feature_names())
            self.assertTrue(self.features["FLAG"])

        self.assertNotIn("FLAG", self.features.get_feature_names())
