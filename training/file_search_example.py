import os
from os.path import isdir, join
from threading import Thread, Lock
import time
matches = []
mutex = Lock()

def file_search(root, filename):
    print(f"Searching in: {root}")
    chile_threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target=file_search,args=([full_path, filename]))
            t.start()
            chile_threads.append(t)
    for t in chile_threads:
        t.join()
            
def main():
    t = Thread(target=file_search,args=(["/drive_data/","README.md"]))
    t.start()
    t.join()
    for m in matches:
        print(f"Matched: {m}")

st = time.time()
main()
en = time.time()
print(f"time taken: \x1b[0:30;41m{en-st}\x1b[0m")
