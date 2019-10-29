"""
Lab 4: Q1d: Reboot an Amazon EC2 instance
"""

import boto3
import sys
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

# Do a dry run first to verify permissions
try:
    ec2.reboot_instances(InstanceIds=['i-0460bdbeab812f1f9'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to reboot instances")
        raise
# Dry run succeeded, run start_instances again without dry run
try:
    response = ec2.reboot_instances(InstanceIds=['i-0460bdbeab812f1f9'], DryRun=False)
    print("Success. ", response)
except ClientError as e:
    print("Error: ", e)
