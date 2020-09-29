# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:08:33 2020

@author: drv_m
"""

import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    invokeLam = boto3.client("lambda", region_name="us-east-2")
    payload = {"message":"You have been invoked !"}
    # If you just want to trigger another lambda without response, use InvocationType="Event" else use InvocationType="RequestResponse"
    resp = invokeLam.invoke(FunctionName="lambdaFunction2", InvocationType="RequestResponse", Payload=json.dumps(payload))
    print(resp["Payload"].read())
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
