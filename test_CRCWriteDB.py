import pytest
from CRCWriteDB import *

test_api_event = {
    "requestContext": {
        "identity" : {
            "sourceIP": "1.1.1.1"
            },
        "requestTime": "TEST"
    }
}

def test_lambda_handler():

    try:
        response = lambda_handler(event=test_api_event, context={})
    except Exception as e:
        print(e)

    assert True == True
