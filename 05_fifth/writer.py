import os
import time
import uuid
from threading import Thread, current_thread, active_count
import redis
from pytask import Task


redis_client = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

def wait_for_it(list_key):
    results = redis_client.brpop(list_key)
    print("survey sez: {}".format(results))
    print("current thread: {}".format(current_thread()))
    print("{} threads total".format(active_count()))

while True:
    time.sleep(1)
    new_task = Task(uuid.uuid1(), uuid.uuid1())
    print("sending {}".format(new_task.json_message()))

    redis_client.publish('incoming', new_task.message["respond_to"])
    redis_client.lpush('effecty', new_task.json_message())

    t = Thread(target=wait_for_it, args=(new_task.message["respond_to"], ))
    t.start()
