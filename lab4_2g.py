"""
Lab 4: Q2g:  Get Bucket Access Control List
"""

import boto3


s3_client = boto3.client('s3')
bucket_name = 'lrc035lab42abuc'
response = s3_client.get_bucket_acl(Bucket=bucket_name)
print(response)
