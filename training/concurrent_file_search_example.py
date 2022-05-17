import os
import time
from os.path import isdir, join
from threading import Thread, Lock
from wait_group import WaitGroup
matches = []
mutex = Lock()

st = time.time()


def file_search(root, filename, wait_group):
    print(f"Searching in: {root}")
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=(
                [full_path, filename, wait_group]))
            t.start()
    wait_group.done()


def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t = Thread(target=file_search, args=(
        ["/drive_data/", "README.md", wait_group]))
    t.start()
    wait_group.wait()
    for m in matches:
        print(f"Matched: \x1b[0;30;42m{m}\x1b[0m")


st = time.time()
main()
en = time.time()
print(f"time taken: \x1b[0:30;41m{en-st}\x1b[0m")
