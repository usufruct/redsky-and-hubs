import time
import sys
import os
import redis
import uuid

queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    print('hello')
    queue.lpush('simple', uuid.uuid1())
    sys.stdout.flush()
    time.sleep(1)
