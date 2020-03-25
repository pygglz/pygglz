import unittest

from pygglz import features


class FeaturesTest(unittest.TestCase):
    def test_it(self):
        with features.new_feature_context():
            pass
