import time
from queue import Queue
from threading import Thread

count = 0


def consumer(q):
    global count
    while count <= 10:
        # while True:
        txt = q.get()
        print(txt)
        time.sleep(1)
        count += 1



def producer(q):
    global count
    # while True:
    while count < 10:
        q.put("hello there")
        print("message sent")
        time.sleep(1)
        count += 1

# q = Queue(maxsize=10)
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
