# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:13:42 2020

@author: drv_m
"""

import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    return {
        'statusCode': 200,
        'body': json.dumps('lambdaFunction2 has been invoked !')
    }
