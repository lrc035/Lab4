"""
Lab 4: Q2b: List existing Amazon S3 Buckets
"""

import boto3

s3_client = boto3.client('s3')
response = s3_client.list_buckets()
# Output bucket names
print('Existing buckets: ')
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')
