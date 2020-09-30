# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 19:55:59 2020

@author: drv_m
"""

import json
import boto3
from pprint import pprint

def lambda_handler(event, context):
    
    # Initiate client for s3 and provide bucketname and key
    s3 = boto3.client("s3")
    bucketName = "lambdaspeech"
    key = "speech.txt"
    file = s3.get_object(Bucket = bucketName, Key = key)
    paragraph = str(file['Body'].read())
    
    comprehend = boto3.client("comprehend")
    #sentiment analysis
    response = comprehend.detect_sentiment(Text = paragraph, LanguageCode = "en")
    # print(response)
    sentimentType = response['Sentiment']
    sentimentScore = response['SentimentScore']
    print(sentimentType)
    print(sentimentScore)
    
    #name entity recognition
    entities = comprehend.detect_entities(Text = paragraph, LanguageCode = "en")
    pprint(entities)
    
    keyphrase = comprehend.detect_key_phrases(Text = paragraph, LanguageCode = "en")
    pprint(keyphrase)
    
    
    return {
        'statusCode': 200,
        'sentiment' : sentimentType,
        'sentimentScoreDict': sentimentScore
    }
