import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Attr
from config import *


def get_resource():
    return boto3.resource('dynamodb',
                              aws_access_key_id=ACCESS_KEY,
                              aws_secret_access_key=SECRET_ACCESS_KEY,
                              region_name=REGION)


def create_sensor_table(dynamodb=None):
    if not dynamodb:
        dynamodb = get_resource()

    table = dynamodb.create_table(
        TableName='Sensors',
        KeySchema=[
            {
                'AttributeName': 'sensorid',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'sensorname',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'sensorid',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'sensorname',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    print("Creating Sensors...")
    return table


def store_Sensors(sensors, dynamodb=None):
    if not dynamodb:
        dynamodb = get_resource()

    table = dynamodb.Table('Sensors')
    for sensor in sensors:
        print(f'Adding sensor {sensor["sensorname"]}')
        table.put_item(Item=sensor)


def get_all_sensors(dynamodb=None):
    if not dynamodb:
        dynamodb = get_resource()

    table = dynamodb.Table('Sensors')

    try:
        response = table.scan()
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']


def get_all_by_sensorname(sensorname, dynamodb=None):
    if not dynamodb:
        dynamodb = get_resource()

    table = dynamodb.Table('Sensors')

    sortkey = Attr('sensorname').eq(sensorname)
    try:
        response = table.scan(FilterExpression=sortkey)
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Items']
