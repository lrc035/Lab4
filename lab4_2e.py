"""
Lab 4: Q2e: Create presigned URLs
"""

import boto3

s3_client = boto3.client('s3')
bucket_name = 'lrc035lab42abuc'
key = 'README.md'
response = s3_client.generate_presigned_url(ClientMethod='get_object', Params={'Bucket':bucket_name, 'Key':key})
print(response)
