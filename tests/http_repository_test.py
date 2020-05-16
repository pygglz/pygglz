import unittest
from unittest.mock import patch

import requests
from mockito import mock

from pygglz.feature_state import FeatureState
from pygglz.http_repository import HttpRepository


class HttpRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = HttpRepository("http://localhost:8080")
        self.get_response = mock({"ok": True, "content": "{\"A\":{\"enabled\":true}}"})
        self.empty_get_response = mock({"ok": True, "content": "{}"})
        self.put_response = mock({"ok": True})

    def test_load(self):
        with patch.object(requests, 'get', return_value=self.get_response):
            feature_state = self.repo.get_feature_state("A")
            self.assertTrue(feature_state.enabled)

    def test_save(self):
        with patch.object(requests, 'get', return_value=self.empty_get_response):
            with patch.object(requests, 'put', return_value=self.put_response) as put_method:
                feature_state = self.repo.set_feature_state(FeatureState("A", enabled=True))
                self.assertEqual(put_method.call_args.args[0], "http://localhost:8080")
                self.assertEqual(put_method.call_args.kwargs["data"], {'A': {'enabled': True}})
