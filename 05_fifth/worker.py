import os
import time
import json
import redis

redis_client = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    job = json.loads(redis_client.brpop('effecty')[1])
    response = job["params"]["secret"][::1]
    respond_to = job["respond_to"]

    timestamp = redis_client.brpop('timestamp:{}'.format(respond_to))[1].decode('utf-8')

    time.sleep(1)

    print(response)

    delta = time.time() - float(timestamp)
    print("time: {}".format(delta))
    redis_client.lpush(respond_to, response)
