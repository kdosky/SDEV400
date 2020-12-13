# add data into table via an array 

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Sensors')
elements = [[1,'Hydrogen'],
            [2,'Helium'],
            [3,'Lithium'],
            [4,'Beryllium'],
            [5,'Boron'],
            [6,'Carbon']]

for element in elements:
    num = element[0]
    name = element[1]

    table.put_item(
        Item={
            'ElemNum': num,
            'ElemName': name
        }
    )