
import os
import uuid
from pathlib import Path
from flask import Flask, request, render_template
from redis import Redis
from face_match import FaceMatch
from interfaces.redis.client import get_connection


def generate_image_uuid(filename_base):
    image_uuid = uuid.uuid4()
    return f'image:{filename_base}:{image_uuid}'

def upload_images():
    redis = get_connection()
    for filename in os.listdir(f'{CURRDIR}/images'):
        if filename.endswith('.png'):
            filename_base = Path(filename).stem
            image = open(f'{CURRDIR}/images/{filename}','rb').read()
            uuid = generate_image_uuid(filename_base)
            redis.set(uuid, image)

app = Flask(__name__)

@app.route('/')
def display_images_list():
    redis = get_connection()
    keys = []
    for key in redis.scan_iter():
        keys.append(key.decode("utf-8"))
    image_list = { 'images': keys }
    if image_list['images']: 
        return render_template('home.html',data = image_list)
    else:
        return 'No such image exists. Please try uploading new images to redis.'

@app.route('/facematch', methods=['POST'])
def face_match():
    request_data = request.get_json()
    image_data = request_data['images']
    face_match = FaceMatch(image_data[0],image_data[1])
    probability = face_match.compare()
    response = {'facematch':request_data,'probability':probability}
    return response
 

if __name__ == "__main__":
    CURRDIR = os.curdir
    upload_images()
    app.run(host="0.0.0.0", port=5000, debug=True)
