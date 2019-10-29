"""
Lab 4: Q1j: Delete a security group
"""

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.delete_security_group(GroupId='sg-0130640eafa2d7c57')
    print("Success. ", response)
except ClientError as e:
    print(e)
        
