import os
import time
import uuid
from threading import Thread, current_thread, active_count
import redis
from pytask import Task


redis_client = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0)

while True:
    time.sleep(1)
    new_task = Task(uuid.uuid1(), uuid.uuid1())
    print("sending {}".format(new_task.json_message()))

    redis_client.lpush('effecty', new_task.json_message())

    result = redis_client.brpop(new_task.message["respond_to"])[1]

    print('got it {}'.format(result))
