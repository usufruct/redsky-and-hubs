import time
import sys
import os
import redis
import uuid
import json
import signal  # unix only


queue = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

class TimeoutException(Exception):
    pass

def timeout_handler(num, stack):
    raise TimeoutException("it took TOO LONG!")

def task():
    task = {}
    task["respond_to"] = str(uuid.uuid1())
    task["params"] = {}
    task["params"]["uuid"] = str(uuid.uuid1())

    return task

signal.signal(signal.SIGALRM, timeout_handler)

while True:
    print('back to top')
    sys.stdout.flush()

    new_task = task()
    respond_to = new_task["respond_to"]
    unique = new_task["params"]["uuid"]
    task_json = json.dumps(new_task)
    queue.lpush('responsive', task_json)

    answer = queue.hget('response_store', respond_to)

    try:
        signal.alarm(1)
        print("looking for {}".format(respond_to))
        sys.stdout.flush()
        while(answer == None):
            time.sleep(0.01)
            answer = queue.hget('response_store', respond_to)
    except TimeoutException as e:
        print('operation timed out')
        print(respond_to)
        sys.stdout.flush()

    if(answer != None):
        print('answer found')
        print(respond_to)
        print(answer)
        sys.stdout.flush()

    print('resetting alarm')
    sys.stdout.flush()
    signal.alarm(0)



