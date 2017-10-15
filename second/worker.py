import time
import sys
import os
import redis
import json


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    print('olleh')
    results = queue.brpop('responsive')
    results_dict = json.loads(results[1])
    response_key = results_dict["respond_to"]
    param = results_dict["params"]["uuid"]
    reversed_param = param[::-1]

    time.sleep(2)

    queue.hset('response_store', response_key, reversed_param)
    print(response_key)
    sys.stdout.flush()

