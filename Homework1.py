# Name: Khoger Dosky
# File Name: homework1.py
# Date: November 3, 2020
# Course: SDEV 400 7381 Secure Programming in the Cloud (2208)
# Dr. Matthew Taylor

import boto3
from datetime import datetime
from pytz import timezone


# welcome print line 
print('*** Python command line menu-driven interface application ***')

# while loop 
while (True):
    # menu selection 
    print('\nSelect AWS S3 functionality: \n'
          '\na. Creates a S3 bucket with the name consisting of your firstname, lastname and a random 6-digit suffix.'
          '\nb. Puts objects in a previously created bucket.'
          '\nc. Deletes an object in a bucket.'
          '\nd. Deletes a bucket.'
          '\ne. Copies and object from one bucket to another.'
          '\nf. Downloads an existing object from a bucket.'
          '\ng. Exit the program. Upon exit, the application should list the date and time.\n')
    
     
    user_input = input('Enter a, b, c, d, e, f or g to run functionality: \n\n')
    s3 = boto3.client('s3')
    tz = timezone('EST')
    now = datetime.now(tz)
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    bucket_name = 'khogerdosky-654321'
    KEY = 'file.txt' 

    # if user selects a
    # Creates a S3 bucket with the name consisting of your firstname, lastname and a random 6-digit suffix
    if user_input == 'a':
        s3.create_bucket(Bucket = bucket_name)
        print('\nBucket', bucket_name,'has been created in Amazon S3')
    
    # if user selects b
    # Puts objects in a previously created bucket
    if user_input == 'b':
        filename = 'file.txt'
        s3.upload_file(filename, bucket_name, filename)
        print('\nObject', filename,'has been added to bucket', bucket_name)
    
    # if user selects c 
    # Deletes an object in a bucket
    if user_input == 'c':
        filename = 'file.txt'
        s3.delete_object(Bucket=bucket_name, Key=filename)
        print('\nObject', filename,'has been deleted from bucket', bucket_name)
    
    # if user selects d
    # Deletes a bucket
    if user_input == 'd':
        s3.delete_bucket(Bucket=bucket_name)
        print('\nBucket', bucket_name,'has been deleted from Amazon S3')
    
    # if user selects e
    # Copies and object from one bucket to another
    if user_input == 'e':
        dest_bucket_name = 'kdosky.bucket1'
        dest_object_name = 'copyfile.txt'
        s3 = boto3.resource('s3')
        s3.Object(dest_bucket_name, dest_object_name).copy_from(CopySource='khogerdosky-654321/file.txt')
        print('\nObject', dest_object_name,'has been copied to Bucket', dest_bucket_name)
    
    # if user selects f
    # Downloads an existing object from a bucket
    if user_input == 'f':
        s3 = boto3.resource('s3')
        bucket_name = 'khogerdosky-654321'
        KEY = 'file.txt' 
        saved_file = 'NewFile.txt'
        s3.Bucket(bucket_name).download_file(KEY, saved_file)
        print('\nObject', KEY, 'from bucket', bucket_name,'has been downloaded and saved as', saved_file)
        
    # exiting app message and prints current date and time 
    # Exit the program. Upon exit, the application should list the date and time
    elif user_input == 'g':
        print('\nYou have exited the application\n')
        print('Current Date and Time:', dt_string)
        break


  
