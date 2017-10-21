import uuid
import time
import os
from threading import Thread
import json
import redis

redis_client = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)


def task(respond_to, uniq):
    task = {}
    task["params"] = {}
    task["respond_to"] = respond_to
    task["params"]["secret"] = uniq

    return task

def wait_for_it(list_key):
    results = redis_client.brpop(list_key)
    print("survey sez: {}".format(results))


while True:
    time.sleep(1)
    respond_to = str(uuid.uuid1())
    secret = str(uuid.uuid1())

    new_task = task(respond_to, secret)
    print("sending {}".format(secret))
    redis_client.lpush('thready', json.dumps(new_task))

    t = Thread(target=wait_for_it, args=(respond_to, ))
    t.start()