import json
import unittest

import boto3

from pygglz.dynamodb import DynamodbRepository
from pygglz.feature_state import FeatureState


class LocalDynamodb(object):
    def __init__(self):
        self.endpoint_url = "http://localhost:4569"
        self.resource = boto3.resource('dynamodb', endpoint_url=self.endpoint_url)
        self.client = boto3.client('dynamodb', endpoint_url=self.endpoint_url)

    def create_schema(self, schema=None):
        table_names = self.client.list_tables()["TableNames"]

        for table_name, table in schema["Tables"].items():
            if table_name in table_names:
                self.client.delete_table(TableName=table_name)

            create_table_args = {
                "TableName": table_name,
                "AttributeDefinitions": table["AttributeDefinitions"],
                "KeySchema": table["KeySchema"],
                "BillingMode": table.get("BillingMode", "PAY_PER_REQUEST")
            }

            self.client.create_table(**create_table_args)

    def load_items(self, items=None):
        for table_name, items in items.items():
            table = self.resource.Table(table_name)
            for item in items:
                table.put_item(Item=item)

    def assert_contains_item(self, table_name=None, key=None):
        table = self.resource.Table(table_name)
        response = table.get_item(TableName=table_name, Key=key)
        if not "Item" in response:
            raise AssertionError("Item with key={} not found in {}.".format(json.dumps(key), table_name))


SCHEMA = {"Tables": {
    "features": {
        "AttributeDefinitions": [
            {
                "AttributeName": "name",
                "AttributeType": "S"
            }
        ],
        "KeySchema": [
            {
                "AttributeName": "name",
                "KeyType": "HASH"
            }
        ]
    }
}}


class DynamodbRepositoryIntegrationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.local_dynamodb = LocalDynamodb()
        self.local_dynamodb.create_schema(SCHEMA)

    def test_get_feature_state(self):
        self.local_dynamodb.load_items(items={"features": [{"name": "F1", "enabled": True}]})
        self.repo = DynamodbRepository(self.local_dynamodb.resource)
        self.assertTrue(self.repo.get_feature_state("F1").enabled)

    def test_set_feature_state(self):
        self.repo = DynamodbRepository(self.local_dynamodb.resource)
        self.repo.set_feature_state(FeatureState("F1", True))
        self.local_dynamodb.assert_contains_item(table_name="features", key={"name": "F1"})
