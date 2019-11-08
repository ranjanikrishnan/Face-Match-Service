import os
import boto3

def get_connection():
	aws_access = os.environ['AWS_ACCESS'].strip('\'')
	aws_secret=os.environ['AWS_SECRET'].strip('\'')
	rekognition = boto3.client("rekognition", region_name='eu-west-1', aws_access_key_id=aws_access, aws_secret_access_key=aws_secret)
	return rekognition
