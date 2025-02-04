import os
import boto3
from interfaces.rekognition import client

def compare_faces(source_bytes, target_bytes, threshold=80):
	
	rekognition = client.get_connection()
	response = rekognition.compare_faces(SourceImage={'Bytes': source_bytes},
		                                 TargetImage={'Bytes': target_bytes},
	                                     SimilarityThreshold=threshold)
	probability_response = response['FaceMatches'][0]['Similarity']/100
	probability = round(probability_response,2)
	return probability
