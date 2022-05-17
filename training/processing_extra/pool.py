from multiprocessing import Pool
import time


def cube(number):
    return number * number * number


if __name__ == '__main__':
    numbers = range(10)
    st = time.time()
    print(list(map(cube, numbers)))
    en = time.time()
    st1 = time.time()
    pool = Pool()
    result = pool.map(cube, numbers)
    pool.close()
    pool.join()
    en1 = time.time()
    print(result)
    print(f"time taken1: {en1-st1}")
    print(f"time taken: {en-st}")
