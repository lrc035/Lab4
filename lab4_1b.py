"""
Lab 4: Q1b: Start and stop detailed monitoring of EC2 instance
"""

import boto3
import sys

ec2 = boto3.client('ec2')
if (sys.argv[1] == 'ON'):
    response = ec2.monitor_instances(InstanceIds=["i-0d74e94a15dd41da6"])
else:
    response = ec2.unmonitor_instances(InstanceIds=["i-0d74e94a15dd41da6"])
print(response)
