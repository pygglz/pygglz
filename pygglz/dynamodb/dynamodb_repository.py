import boto3
from botocore.exceptions import ClientError

from ..feature_state import FeatureState
from ..state_repository import StateRepository


class DynamodbRepository(StateRepository):
    def __init__(self, dynamodb_resource=None, table_name="features"):
        self.table_name = table_name
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
                feature_name = item["featureName"]
                feature_state = item["featureState"]
                yield FeatureState(feature_name, feature_state.get("enabled", False))

            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items = response.get('Items', [])
                for item in items:
                    feature_name = item["featureName"]
                    feature_state = item["featureState"]
                    yield FeatureState(feature_name, feature_state.get("enabled", False))
        except ClientError as e:
            if e.response["Error"]["Code"] != 'ResourceNotFoundException':
                raise

    def save(self, feature_state):
        table = self.dynamodb_resource.Table(self.table_name)
        table.put_item(Item={
            "featureName": feature_state.name,
            "featureState": {
                "enabled": feature_state.enabled
            }
        })
