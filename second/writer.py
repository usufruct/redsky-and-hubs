import time
import sys
import os
import redis
import uuid
import json


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

def task():
    task = {}
    task["respond_to"] = str(uuid.uuid1())
    task["params"] = {}
    task["params"]["uuid"] = str(uuid.uuid1())

    return task

while True:
    print('hello')

    new_task = task()
    respond_to = new_task["respond_to"]
    unique = new_task["params"]["uuid"]
    task_json = json.dumps(new_task)
    queue.lpush('responsive', task_json)

    answer = queue.hget('response_store', respond_to)

    while(answer == None):
        time.sleep(0.01)
        answer = queue.hget('response_store', respond_to)

    print('answer found')
    print(answer)

    sys.stdout.flush()
