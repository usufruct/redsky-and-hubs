import time
import sys
import os
import redis
import json
import random


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    results = queue.brpop('responsive')
    results_dict = json.loads(results[1])
    response_key = results_dict["respond_to"]
    param = results_dict["params"]["uuid"]
    reversed_param = param[::-1]

    # random sleep from .001 -> 2 seconds
    sleep_time = random.randint(1, 1000)
    print("sleeping for {} milliseconds".format(sleep_time))
    print(response_key)
    sys.stdout.flush()

    time.sleep(sleep_time/1000)

    queue.hset('response_store', response_key, reversed_param)

