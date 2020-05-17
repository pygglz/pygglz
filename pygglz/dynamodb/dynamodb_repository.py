from typing import Callable

import boto3
from botocore.exceptions import ClientError

from ..feature_state import FeatureState
from ..state_repository import StateRepository


def default_from_item(item) -> FeatureState:
    feature_name = item["featureName"]
    feature_state = item["featureState"]
    return FeatureState(feature_name, feature_state.get("enabled", False))


def default_to_item(feature_state: FeatureState) -> dict:
    return {
        "featureName": feature_state.name,
        "featureState": {
            "enabled": feature_state.enabled
        }
    }


class DynamodbRepository(StateRepository):
    def __init__(self, dynamodb_resource=None,
                 table_name: str = "features",
                 from_item_func: Callable = default_from_item,
                 to_item_func: Callable = default_to_item):
        self.table_name = table_name
        self.from_item_func: Callable = from_item_func
        self.to_item_func: Callable = to_item_func
        self.dynamodb_resource = dynamodb_resource or boto3.resource("dynamodb")
        super().__init__()

    def load(self):
        return {f.name: f for f in self.__scan_features()}

    def __scan_features(self):
        try:
            table = self.dynamodb_resource.Table(self.table_name)
            response = table.scan()
            items = response.get('Items', [])
            for item in items:
                yield self.from_item_func.__call__(item)

            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items = response.get('Items', [])
                for item in items:
                    yield self.from_item_func.__call__(item)
        except ClientError as e:
            if e.response["Error"]["Code"] != 'ResourceNotFoundException':
                raise

    def save(self, feature_state):
        table = self.dynamodb_resource.Table(self.table_name)
        item = self.to_item_func.__call__(feature_state)
        table.put_item(Item=item)
