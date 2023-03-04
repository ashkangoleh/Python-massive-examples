# SuperFastPython.com
# example of a nested for-loop to use a single shared thread pool
import time
import multiprocessing.pool
 
# third level task
def task3(arg):
    # report message
    print(f'\t\t>>>task3 {arg}')
    # do work
    time.sleep(1)
 
# second level task
def task2(arg):
    # declare the global pool
    global pool
    # report message
    print(f'\t>>task2 {arg}')
    # do work
    time.sleep(1)
    # issue third level tasks and wait
    pool.map(task3, range(2))
 
# top level task
def task1(arg):
    # declare the global pool
    global pool
    # report message
    print(f'>task1 {arg}')
    # do work
    time.sleep(1)
    # issue second level tasks and wait
    pool.map(task2, range(3))
 
# protect the entry point
if __name__ == '__main__':
    # declare global pool
    global pool
    # assign the global pool
    pool = multiprocessing.pool.ThreadPool(100)
    # issue top level tasks to pool and wait
    pool.map(task1, range(10000))
    # close the pool
    pool.close()