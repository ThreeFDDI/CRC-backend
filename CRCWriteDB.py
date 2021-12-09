import json
import boto3

AWS_REGION = 'us-east-1'

def lambda_handler(event, context):

    client = boto3.resource("dynamodb", region_name=AWS_REGION)
    
    table = client.Table("CRC_visitors")
    
    table.put_item(Item = {
        "visitor_number": event["requestContext"]["identity"]["sourceIp"], 
        "time": event["requestContext"]["requestTime"]
        })
    
    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'https://resume.threefddi.net',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        "body": json.dumps(table.item_count)
    }

