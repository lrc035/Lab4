"""
Lab 4: Q1f: Create a new key pair
"""

import boto3

ec2 = boto3.client('ec2')

response = ec2.create_key_pair(KeyName='lrc035Lab41fKey')
print("Success. ", response)
