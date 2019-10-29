"""
Lab 4: Q1h: Get info abot security groups
"""

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.describe_security_groups(GroupIds=['sg-09559c27287ac0ec0'])
    print("Success. ", response)
except ClientError as e:
    print(e)
        
