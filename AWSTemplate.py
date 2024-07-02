"""
AWS Operations with Boto3

This script demonstrates basic operations using Boto3 to interact with AWS services.
It performs operations such as uploading and downloading files from S3, launching and
terminating EC2 instances.

🛠️ Installation Steps:
1. Install Boto3
   pip install boto3

2. AWS Credentials Setup
   Ensure AWS credentials are configured either through environment variables, AWS CLI,
   or IAM roles if running on an AWS resource.

"""

import boto3

# Create an S3 client object
s3 = boto3.client('s3')

# Upload a file to S3
bucket_name = 'my-bucket-name'
file_name = 'path/to/local/file.txt'
object_name = 'file.txt'

s3.upload_file(file_name, bucket_name, object_name)

# Download a file from S3
bucket_name = 'my-bucket-name'
object_name = 'file.txt'
file_name = 'path/to/local/file.txt'

s3.download_file(bucket_name, object_name, file_name)

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Launch an EC2 instance
image_id = 'ami-0c55b159cbfafe1f0'
instance_type = 't2.micro'
key_name = 'my-key-pair'

response = ec2.run_instances(ImageId=image_id, InstanceType=instance_type, KeyName=key_name)

# Terminate an EC2 instance
instance_id = 'i-0123456789abcdef0'

ec2.terminate_instances(InstanceIds=[instance_id])
