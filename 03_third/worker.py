import os
import time
import redis
import json


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    results = queue.brpop('jobs')
    results_dict = json.loads(results[1])

    response_key = results_dict["respond_to"]
    secret_param = results_dict["params"]["secret"]
    print('job recieved {}'.format(response_key))
    time.sleep(1)

    reversed_param = secret_param[::-1]

    print("pushing response")
    queue.lpush(response_key, reversed_param)
