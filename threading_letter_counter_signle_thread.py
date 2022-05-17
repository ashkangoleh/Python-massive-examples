import json
import urllib.request
import time
from threading import Thread, Lock

finished_count = 0

def count_letters(url, frequency, mutex):
    response = urllib.request.urlopen(url)
    txt = str(response.read())
    mutex.acquire()
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1
    global finished_count
    finished_count += 1
    mutex.release()


def main():
    frequency = {}
    mutex = Lock()
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    st = time.time()
    for i in range(1000, 1020):
        Thread(target=count_letters, args=(
            f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency, mutex)).start()
        # count_letters(f"https://www.rfc-editor.org/rfc/rfc{i}.txt", frequency)
    
    while finished_count < 20:
        time.sleep(0.5)
    
    en = time.time()
    print(json.dumps(frequency, indent=4))
    print(f"Done, time taken = {en-st:0.02f}")


main()
