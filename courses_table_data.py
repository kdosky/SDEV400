# Name: Khoger Dosky
# File Name: courses_table_data.py
# Date: November 17, 2020
# Course: SDEV 400 7381 Secure Programming in the Cloud (2208)
# Dr. Matthew Taylor

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Courses')
elements = [[1,400,3,'SDEV','Secure Programming in the Cloud'],
            [2,334,3,'ARTH','Understanding Movies'],
            [3,100,3,'CCJS','Introduction to Criminal Justice'],
            [4,201,3,'ECON','Principles of Macroeconomics'],
            [5,141,3,'CMIS','Introductory Programming'],
            [6,326,3,'ACCT','Accounting Information Systems'],
            [7,290,3,'CMST','Introduction to Interactive Design'],
            [8,200,3,'STAT','Introduction to Statistics'],
            [9,105,3,'MATH','Topics for Mathematical Literacy'],
            [10,112,3,'WRTG','Academic Writing II']]
for element in elements:
    num = element[0]
    num2 = element[1]
    num3 = element[2]
    name = element[3]
    name2 = element[4]
    table.put_item(
        Item={
            'CourseID': num,
            'CatalogNbr': num2,
            'NumCredits': num3,
            'Subject': name,
            'Title': name2
            
        }
    )