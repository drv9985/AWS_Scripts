# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 12:49:51 2020

@author: drv_m
"""
import json
import boto3

def lambda_handler(event, context):
    try:
        s3 = boto3.client("s3")
    except Exception as e:
        print("Error during s3 client creation: {}".format(e))
    
    try:
        print("Event : {}".format(event))
        file_obj = event["Records"][0]
        bucketName = str(file_obj['s3']['bucket']['name'])
        filename = str(file_obj['s3']['object']['key'])
        print('Bucketname is {}'.format(bucketName))
        print('Filename is {}'.format(filename))
        fileObj = s3.get_object(Bucket = bucketName, Key = filename)
        fileContent = fileObj['Body'].read().decode('utf-8')
        print(fileContent)
        
    except Exception as e:
        print("Error during module execution: {}".format(e))
