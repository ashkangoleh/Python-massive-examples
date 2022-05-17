from blocks import main as mb
from inputs import main as mi
from transactions import main as mt
# import multiprocessing
# import time
from subprocess import Popen
import os
Popen(f"{os.getcwd()}/blocks.py")
Popen(f"{os.getcwd()}/transactions.py")
Popen(f"{os.getcwd()}/inputs.py")
Popen(f"{os.getcwd()}/outputs.py")



# _mb = multiprocessing.Process(target=mb)
# _mt = multiprocessing.Process(target=mt)


# if __name__=="__main__":
#     _mb.start()
#     _mt.start()
#     _mt.join()
#     _mb.join()
    
# final = time.perf_counter()
# print('final: ', final)
