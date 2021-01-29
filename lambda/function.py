import json
import boto3


def handler(event, context):
    '''When this function is invoked - retrive visitor count, add one, store
    in database, return to client '''
    dynamodb = boto3.client('dynamodb')

    # Get Visits
    response = dynamodb.get_item(TableName='stuartsresumecounter', Key={'Site': {'N': '0'}})

    visits = int(response["Item"]["Visits"]["N"]) + 1

    # Store Visits
    dynamodb.put_item(TableName='stuartsresumecounter', Item={
        'Site': {'N': '0'},
        'Visits': {'N': str(visits)}
    })
    return visits
