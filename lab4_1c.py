"""
Lab 4: Q1c: Start and stop an Amazon EC2 instance
"""

import boto3
import sys
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')
action = sys.argv[1].upper();

if (action == "ON"):
    # Do a dry run first to verify permissions
    try:
        ec2.start_instances(InstanceIds=['i-0460bdbeab812f1f9'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances again without dry run
    try:
        response = ec2.start_instances(InstanceIds=['i-0460bdbeab812f1f9'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
else:
    # Do a dry run first to verify permissions
    try:
        ec2.stop_instances(InstanceIds=['i-0460bdbeab812f1f9'], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise
    # Dry run succeeded, run start_instances again without dry run
    try:
        response = ec2.stop_instances(InstanceIds=['i-0460bdbeab812f1f9'], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
