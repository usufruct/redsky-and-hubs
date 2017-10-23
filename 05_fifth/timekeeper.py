import os
import time
import redis


redis_client = redis.StrictRedis(host='localhost', port=os.environ.get('REDIS_PORT'), db=0, charset="utf-8", decode_responses=True)
subsciber = redis_client.pubsub()
subsciber.subscribe('incoming')

for incomer in subsciber.listen():
    timekey = 'timestamp:{}'.format(str(incomer['data']))
    redis_client.lpush(timekey, time.time())



