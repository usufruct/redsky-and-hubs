## Reinventing the World One Wheel at a Time

The pieces

* redis (messaging)
* json (message format)
* python (logic)
* ruby (foreman)
* Make (tasks)

# 01_First

* writer
* worker
* no message response

Writer(s) put a message onto queue and Worker(s) recieve the message.

# 02_Second

* writer
* worker
* writer waits for an answer

Writer(s) put a message onto a queue. Worker(s) pull messages off the queue. Worker places answer into a
channel which is identified to a unique key provided by the Writer. Writer polls response channel, and times out if there is no answere withing a time limit set by the Worker.

# 03_Third

* writer
* worker
* writer waits for an answer

Writer(s) put messages onto a queue. Worker(s) pull messages off. Once 'work' is done, worker places answer into a queue of one, named for a unique response keys provided in the message. Writer blocks on the response channel.






