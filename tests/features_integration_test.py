import unittest

from pygglz import features


class FeaturesTest(unittest.TestCase):
    def test_it(self):
        self.assertFalse(features["FLAG"])
        features.set_feature_enabled("FLAG", False)
        self.assertFalse(features["FLAG"])

        with features.new_feature_context(read_only=False):
            self.assertFalse(features["FLAG"])
            features.set_feature_enabled("FLAG")
            self.assertTrue(features["FLAG"])

        self.assertFalse(features["FLAG"])
