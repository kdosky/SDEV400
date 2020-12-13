import boto3

def lambda_handler(event, context):
    message = processRecords(event)
    
    return {
        'message' : message
    }
def processRecords(myevent):
    region=""
    mytime=""
    vers= ""
    filenamed= ""
    foundIt='false'
    # Looop through event Records
    
    # Assign variable
    for record in myevent['Records']:
        region=record['awsRegion']
        mytime=record['eventTime']
        vers= record['s3']['s3SchemaVersion']
        filenamed = record['s3']['object']['key']
    
    if filenamed =='Tester.dat':
        print('Tester.dat was uploaded')
        foundIt='true'
    
    # Prepare the Message
    message = ' Data: {} {} {} found file is {} '.format(Lambda Function Test Configurations
        filenamed,
        region,
        mytime,
        foundIt
        )
    return message