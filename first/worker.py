import time
import sys
import os
import redis


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    print('olleh')
    results = queue.brpop('simple')
    print(results)

