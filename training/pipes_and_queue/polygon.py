import re
import random
import time
from multiprocessing import Process
from threading import Thread
count = 0
steper = 1000
file_location = "./polygons.txt"


def polygon_maker(file_root):
    global count, steper
    while count <= 10000000000000000000000:
        polygons = "(" + str(random.randint(0, 999)) + \
            "," + str(random.randint(0, 999))+"),"

        with open(file_root, 'a+') as file:
            file.write(polygons)
            if count == steper:
                file.write("\n")
                steper += 1000
        count += 1


if __name__ == '__main__':
    start = time.time()
    p = Thread(target=polygon_maker, args=(file_location,))
    p.start()
    end = time.time()
    print(f"time taken -> {end - start}")
