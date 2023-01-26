import os
import boto3
import json
from tenable.sc import TenableSC

sc_url = os.getenv('SC_HOST')
tenable_secret_name = os.getenv('TENABLE_SECRET_NAME')
client = boto3.client('secretsmanager')

# function to retrieve api token from aws secret manager
def retrieve_tenable_token(tenable_secret_name):
    response = client.get_secret_value(
        SecretId=tenable_secret_name
    )
    access_key  = json.loads(response["SecretString"])["access_key"]
    secret_key  = json.loads(response["SecretString"])["secret_key"]
    return {"accessKey": access_key, "secretKey": secret_key}

sc_tokens = retrieve_tenable_token(tenable_secret_name)
#initialize tenable
sc = TenableSC(sc_url,access_key=sc_tokens["accessKey"],secret_key=["secretKey"])
print(sc.login())