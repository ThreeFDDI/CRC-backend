import json
import os
import unittest
import boto3
import mock
from moto import mock_dynamodb2

DEFAULT_REGION = 'us-east-1'

DYNAMODB_TABLE_NAME = 'CRC_visitors'

@mock_dynamodb2
@mock.patch.dict(os.environ, {'DB_TABLE_NAME': DYNAMODB_TABLE_NAME})
class TestLambdaFunction(unittest.TestCase):

    def setUp(self):

        # DynamoDB setup
        self.dynamodb = boto3.client('dynamodb', region_name=DEFAULT_REGION)
        try:
            self.table = self.dynamodb.create_table(
                TableName=DYNAMODB_TABLE_NAME,
                KeySchema=[
                    {'KeyType': 'HASH', 'AttributeName': 'visitor_number'}
                ],
                AttributeDefinitions=[
                    {'AttributeName': 'visitor_number', 'AttributeType': 'S'}
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )
        except self.dynamodb.exceptions.ResourceInUseException:
            self.table = boto3.resource('dynamodb', region_name=DEFAULT_REGION).Table(DYNAMODB_TABLE_NAME)

    def test_handler(self):
        from CRCWriteDB import lambda_handler

        events = [
                    {
                        "requestContext": {
                        "requestTime": "01/Dec/2029:23:09:04 +0000",
                        "identity": {
                            "sourceIp": "1.1.1.1",
                            },
                        }
                    },
                    {
                        "requestContext": {
                        "requestTime": "02/Dec/2029:23:09:04 +0000",
                        "identity": {
                            "sourceIp": "2.2.2.2",
                            },
                        }
                    },
                    {
                        "requestContext": {
                        "requestTime": "03/Dec/2029:23:09:04 +0000",
                        "identity": {
                            "sourceIp": "3.3.3.3",
                            },
                        }
                    },
                    {
                        "requestContext": {
                        "requestTime": "04/Dec/2029:23:09:04 +0000",
                        "identity": {
                            "sourceIp": "4.4.4.4",
                            },
                        }
                    }
                ]

        for i in range(len(events)):
            result = lambda_handler(events[i], {})
            count = str(i + 1)

            self.assertEqual(result, {'statusCode': 200, 
                    'headers': {'Access-Control-Allow-Headers': 'Content-Type', 
                        'Access-Control-Allow-Origin': 'https://resume.threefddi.net', 
                        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'}, 'body': count})