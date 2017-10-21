import uuid
import os
import time
import redis
import json


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

def task(respond_to, unique):
    task = {}
    task["params"] = {}
    task["respond_to"] = respond_to
    task["params"]["secret"] = unique

    return task

while True:
    respond_to = str(uuid.uuid1())
    new_task = task(respond_to, str(uuid.uuid1()))
    time.sleep(1.1)
    print('sending job {}'.format(respond_to))
    queue.lpush('jobs', json.dumps(new_task))
    results = queue.brpop(respond_to)

    print(results)