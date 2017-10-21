import os
import time
import redis
import json


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    results = queue.brpop('jobs')
    print('job recieved')
    time.sleep(2)
    results_dict = json.loads(results[1])

    response_key = results_dict["respond_to"]
    secret_param = results_dict["params"]["secret"]

    reversed_param = secret_param[::-1]

    queue.lpush(response_key, reversed_param)
