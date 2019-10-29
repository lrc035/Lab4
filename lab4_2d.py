"""
Lab 4: Q2d: Download files from an Amazon S3 Buckets
"""

import boto3
import botocore

s3 = boto3.resource('s3')
key = 'README.md'
filename = 'README2.md'
bucket_name = 'lrc035lab42abuc'
s3.Bucket(bucket_name).download_file(key, filename)
