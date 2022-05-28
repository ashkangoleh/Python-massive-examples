from multiprocessing.context import Process
from time import sleep, time
import multiprocessing as mp


def do_work():
    print("Starting Work!", end='\n')
    sleep(1)
    print("Finishing Work!", end='\n')


if __name__ == '__main__':
    mp.set_start_method("spawn")
    for _ in range(200):
        p = mp.Process(target=do_work, args=())
        p.start()
