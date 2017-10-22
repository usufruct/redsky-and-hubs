import os
import time
import json
import redis

redis_client = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    time.sleep(1)
    job = json.loads(redis_client.brpop('effecty')[1])

    response = job["params"]["secret"][::1]
    respond_to = job["respond_to"]

    print(response)
    redis_client.lpush(respond_to, response)
