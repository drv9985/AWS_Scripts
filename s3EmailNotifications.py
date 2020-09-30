# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:17:13 2020

@author: drv_m
"""

import json
import boto3

def lambda_handler(event, context):
    print(event)
    # TODO implement
    for i in event["Records"]:
        action = i["eventName"]
        ip = i["requestParameters"]["sourceIPAddress"]
        bucket_name = i["s3"]["bucket"]["name"]
        object = i["s3"]["object"]["key"]
        
    # initiate ses client for email generation
    client = boto3.client("ses")
    subject = "{} event on {} from IP Address {} .".format(str(action),bucket_name,ip)
    body = """
            <br>
            This email is to notify you regarding {} event in {} bucket from source IP:{}
            """.format(str(action), bucket_name, ip)
    
    # configure message payload
    message = {"Subject": {"Data": subject}, "Body":{"Html":{"Data": body}}}
    
    response = client.send_email(Source = "drv.muk@gmail.com", Destination = {"ToAddresses":["dhrubo.office@gmail.com"]}, Message = message)
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Email has been sent')
    }
