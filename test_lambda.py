import os
import json

def lambda_handler(event, context):
    first_name = event['first_name']
    last_name  = event['last_name']
    country    = os.environ['COUNTRY']
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello I am %s %s and I am from %s'%(first_name, last_name, country))
    }
