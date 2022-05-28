from time import sleep, time
from threading import Thread


def do_work():
    print("Starting Work!", end='\n')
    i = 0
    for _ in range(2000000):
        i += 1
    print("Finishing Work!", end='\n')


for i, _ in enumerate(range(5)):
    st = time()
    t = Thread(target=do_work, args=(), daemon=True, name='threading')
    t.start()
    en = time()
print(f"time taken = {en - st}", end='\n')
