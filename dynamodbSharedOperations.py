import boto3
from boto3.dynamodb.conditions import Key, Attr

class Database_Operations:
    def dynamodb_initialization(table_name):
        try:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table(table_name)
            return table
        except Exception as e: 
            return e
    
    def dynamodb_putitem(table, data):
        try:
            table = table
            table.put_item(
                   Item= data
                )
            return print('Item insert successful')
        except Exception as e: 
            return e
    
    def dynamodb_getitem(table, key, value):
        try:
            response = table.get_item(
                Key={
                    key: value
                }
            )
            item = response['Item']
            return item
        except Exception as e: 
            return e
    
    def dynamodb_deleteitem(table, key, value):
        try:
            table.delete_item(
                Key={
                    key: value
                }
            )
            return print('Item deletion successful')
        except Exception as e: 
            return e

    def dynamodb_getallitem(table):
        try:
            response = table.scan()
            items = response['Items']
            return items
        except Exception as e: 
            return e
        
    def dynamodb_scanstring(table, key, value):
        try:
            response = table.scan(
                FilterExpression=Attr(key).eq(value)
            )
            items = response['Items']
            return items
        except Exception as e: 
            return e
    
    def dynamodb_scannumber(table, key, value):
        try:
            response = table.scan(
                FilterExpression=Attr(key).lt(value)
            )
            items = response['Items']
            return items
        except Exception as e: 
            return e