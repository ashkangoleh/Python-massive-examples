import time
import redis
import logging

r = redis.Redis("arz.local", username="default", password="ashkan")

r.flushdb()

key = 'num'
logging.basicConfig()

n = 1

while n <= 100:
    data = {
        "n": n
    }
    msg_id = r.xadd(key, data)
    time.sleep(0.1)
    print("length: ", r.xlen(key))
    print("Memory Usage: ", r.memory_usage(key))
    print(f"Produced the number {n} as message id {msg_id}")
    n += 1
