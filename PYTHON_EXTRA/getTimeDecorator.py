"""
Get time decorator
"""
import time
import logging

logging.basicConfig(
    format="%(asctime)s \033[92m%(message)s\033[0m",
    level=logging.INFO,
)

def get_time(func):
    def inner_get_time(*args, **kwargs) -> str:
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        return (f"Execution time: {(end_time-start_time)*1000:.5f} ms")
    return inner_get_time



@get_time
def test(n):
    loop = [i for i in range(0,n)]
    return loop


print(test(10000000))