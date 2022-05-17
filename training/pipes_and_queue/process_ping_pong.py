from multiprocessing import Process,Pipe
import time


def ping(pipe_conn):
    while(1):
        pipe_conn.send(['ping',time.time()])
        pong = pipe_conn.recv()
        print(pong)
        time.sleep(1)
        
def pong(pipe_conn):
    while(1):
        ping = pipe_conn.recv()
        print(ping)
        time.sleep(1)
        pipe_conn.send(['pong',time.time()])
        
if __name__ == '__main__':
    pip_end_a, pip_end_b = Pipe()
    Process(target=ping,args=(pip_end_a,)).start()
    Process(target=pong,args=(pip_end_b,)).start()
