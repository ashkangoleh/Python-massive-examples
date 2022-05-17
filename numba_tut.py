import numba
import random
import time
import ray

# @numba.jit(nopython=True,parallel=True)
# @numba.jit(parallel=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in numba.prange(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


start = time.time()
print(monte_carlo_pi(10_000_000))
print(time.time()-start)
