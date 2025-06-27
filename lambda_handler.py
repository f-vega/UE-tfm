import boto3
import json

s3 = boto3.client('s3')

BUCKET_NAME = 'fvegadigitaltwinbucket'
OBJECT_KEY = 'latest_machine_data.json' 

def lambda_handler(event, context):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)
    content = response['Body'].read().decode('utf-8')
    data = json.loads(content)
    
    return {
        "propertyValues": {
            "temperature": {
                "value": {
                    "doubleValue": data.get("temperature_c", 0.0)
                }
            },
            "vibration": {
                "value": {
                    "doubleValue": data.get("vibration_ms2", 0.0)
                }
            }
        }
    }