import os
import boto3

def get_connection():
	# aws_access='AKIAT4T4WB4ZFNXOY7PE'
	# aws_secret='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'
	
	aws_access = str(os.environ['AWS_ACCESS'])
	aws_secret= str(os.environ['AWS_SECRET'])
	rekognition = boto3.client("rekognition", region_name='eu-west-1', aws_access_key_id=aws_access, aws_secret_access_key=aws_secret)
	return rekognition
