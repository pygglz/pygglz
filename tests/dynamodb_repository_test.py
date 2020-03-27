import unittest

from mockito import mock, when, verify

from pygglz.dynamodb_repository import DynamodbRepository
from pygglz.feature_state import FeatureState


class DynamodbRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.table_name = "table-name"
        self.dynamodb_resource = mock()
        self.table = mock()
        when(self.dynamodb_resource).Table(self.table_name).thenReturn(self.table)

    def test_load(self):
        when(self.table).scan().thenReturn({"Items": [{"name": "f1", "enabled": True}]})
        self.repo = DynamodbRepository(dynamodb_resource=self.dynamodb_resource, table_name=self.table_name)
        self.assertTrue(self.repo.get_feature_state("f1").enabled)

    def test_save(self):
        when(self.table).scan().thenReturn({"Items": []})
        self.repo = DynamodbRepository(dynamodb_resource=self.dynamodb_resource, table_name=self.table_name)
        self.repo.set_feature_state(FeatureState("f1", True))
        verify(self.table).put_item(Item={"name": "f1", "enabled": True})
