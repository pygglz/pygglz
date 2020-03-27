import unittest

from pygglz import features


class FeaturesTest(unittest.TestCase):
    def test_sub_context_is_isolated(self):
        self.assertNotIn("FLAG", features.get_feature_names())

        with features.new_feature_context(read_only=False):
            self.assertNotIn("FLAG", features.get_feature_names())
            self.assertFalse(features["FLAG"])
            features.set_feature_enabled("FLAG")
            self.assertIn("FLAG", features.get_feature_names())
            self.assertTrue(features["FLAG"])

        self.assertNotIn("FLAG", features.get_feature_names())
