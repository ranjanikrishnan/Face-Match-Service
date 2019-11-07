
import os
import uuid
from flask import Flask, request, jsonify
from redis import Redis
from face_match import FaceMatch
from interfaces.redis.client import get_connection

# CURRDIR = os.path.dirname(__file__)

def generate_image_uuid(filename):
    image_uuid = uuid.uuid4()
    return f'image:{filename}:{image_uuid}'

def upload_images():
    redis = get_connection()
    for filename in os.listdir('./images'):
        if filename.endswith('.png'):
            image = open(f'./images/{filename}','rb').read()
            uuid = generate_image_uuid(filename)
            redis.set(uuid, image)

app = Flask(__name__)

@app.route('/')
def hello():
    return '.'

@app.route('/facematch', methods=['POST'])
def face_match():
    request_data = request.get_json()
    image_data = request_data['images']
    face_match = FaceMatch(image_data[0],image_data[1])
    probability = face_match.compare()
    response = {'facematch':request_data,'probability':probability}
    return response

@app.route('/display-images-list')
def display_images_list():
    redis = get_connection()
    keys = []
    for key in redis.scan_iter():
        keys.append(key.decode("utf-8"))
    return { 'images': keys }
 

if __name__ == "__main__":
    upload_images()
    app.run(host="0.0.0.0", port=5000, debug=True)
