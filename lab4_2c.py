"""
Lab 4: Q2c: Upload filess to an Amazon S3 Buckets
"""

import boto3

s3_client = boto3.client('s3')
filename = 'README.md'
bucket_name = 'lrc035lab42abuc'
s3_client.upload_file(filename, bucket_name, filename)
