# Name: Khoger Dosky
# File Name: courses_table.py
# Date: November 17, 2020
# Course: SDEV 400 7381 Secure Programming in the Cloud (2208)
# Dr. Matthew Taylor

# create courses table 
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='Courses',
    KeySchema=[
        {
            'AttributeName': 'CourseID',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'CourseID',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
print("Table status:", table.table_status)