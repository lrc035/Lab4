"""
Lab 4: Q1i: Create security group
"""

import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

try:
    response = ec2.create_security_groups(GroupName='Lab4_1i', Description='Lab4_1i created 10/29/19')
    print("Success. ", response)
except ClientError as e:
    print(e)
        
