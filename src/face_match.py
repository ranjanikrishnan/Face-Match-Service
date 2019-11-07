from redis import Redis
from interfaces.redis.client import get_connection
from interfaces.rekognition import rekognition

class FaceMatch:
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.client = get_connection()

    def load_images(self):
        source_binary = self.client.get(self.source)
        target_binary = self.client.get(self.target)
        return source_binary, target_binary

    def compare(self):
        source_binary, target_binary = self.load_images()
        probability = rekognition.compare_faces(source_binary, target_binary)
        return probability
