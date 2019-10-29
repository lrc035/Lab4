"""
Lab 4: Q2f: Retrieve a bucket policy
"""

import boto3

s3_client = boto3.client('s3')
bucket_name = 'lrc035lab42abuc'
response = s3_client.get_bucket_policy(Bucket=bucket_name)
print(response['Policy'])
