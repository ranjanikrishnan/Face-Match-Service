import os
from redis import Redis

def get_connection():
    redis = Redis(host=os.environ.get('REDIS_HOST'), port=os.environ.get('REDIS_PORT'))
    return redis