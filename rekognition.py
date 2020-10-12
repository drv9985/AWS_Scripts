# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:29:37 2020

@author: drv_m
"""

import json
import boto3

def lambda_handler(event, context):
    
    reko_client = boto3.client('rekognition')
    response = reko_client.detect_labels(Image = {"S3Object" : {"Bucket" : "rekognition-lambda", "Name" : "image.jpg"}}, MaxLabels = 3, MinConfidence = 80)
    print(response)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
