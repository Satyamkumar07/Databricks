# Databricks notebook source
import boto3

access_key = ""
secret_key = ""

# Create S3 client
s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# List buckets
response = s3_client.list_buckets()
buckets = response['Buckets']
for bucket in buckets:
    print(bucket['Name'])

print(buckets)


