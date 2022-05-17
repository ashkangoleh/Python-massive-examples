import time
from multiprocessing import Queue, Process

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
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=consumer, args=(q,))
    p2 = Process(target=producer, args=(q,))
    p1.start()
    p2.start()
