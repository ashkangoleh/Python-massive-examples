from multiprocessing import Process, Value, Array, Lock
import time


# def add_100(number, lock):
#     for i in range(100):
#         time.sleep(0.1)
#         lock.acquire()
#         number.value += 1
#         lock.release()

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.1)
        for i in range(numbers.__len__()):
            with lock:
                numbers[i] += 1


if __name__ == '__main__':
    lock = Lock()
    # shared_number = Value('i', 0)
    # print(f"Number at beginning is {shared_number.value}")

    # p1 = Process(target=add_100, args=(shared_number, lock))
    # p2 = Process(target=add_100, args=(shared_number, lock))

    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    # print(f"Number at end is {shared_number.value}")
    shared_array = Array('d', [0.0, 100.0, 200.0, 300.0])
    print(f"Number at beginning is {shared_array[:]}")

    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Number at end is {shared_array[:]}")
