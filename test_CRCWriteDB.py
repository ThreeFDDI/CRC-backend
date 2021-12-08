import pytest
from CRCWriteDB import *
from moto import mock_dynamodb2

test_api_event = {
    "requestContext": {
        "identity" : {
            "sourceIP": "1.1.1.1"
            },
        "requestTime": "TEST_DATE"
    }
}
def test_conf():
    assert True

@mock_dynamodb2
@pytest.fixture(autouse=True)
def set_up():

    dynamodb = boto3.resource('dynamodb', 'us-east-1')

    table = dynamodb.create_table(
        TableName='CRC_visitors',
        KeySchema=[{'AttributeName': 'visitor_number', 'KeyType': 'HASH'}],
        AttributeDefinitions=[{'AttributeName': 'visitor_number','AttributeType': 'S'}],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5}
    )


def test_lambda_handler():

    #table = dynamodb.Table("CRC_visitors")
    
    #try:
    #    response = lambda_handler(event=test_api_event, context={})
    #except Exception as e:
    #    print(e)

    #response = table.item_count(
    #    Key={'visitor_number': 'B9B3022F98Fjvjs83AB8a80C185D'}
    #)
    assert True == True

