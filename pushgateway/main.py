import asyncio
import threading
from prometheus_client import CollectorRegistry, Gauge, Counter, pushadd_to_gateway


registry = CollectorRegistry()

counter = Counter(
    name="its_name_for_metrics",
    documentation="its help for counter tracking",
    labelnames=['status', 'method'],
    registry=registry
)


def set_interval(function: callable, interval: int, event_loop: bool = False):
    def _wrapper():
        if event_loop:
            loop = asyncio.new_event_loop()
            set_interval(function, interval, event_loop, )
            loop.run_until_complete(function())
        else:
            set_interval(function, interval, event_loop, )
            function()

    th = threading.Timer(interval, _wrapper)
    th.start()
    return th


def func(*args):
    counter.labels('success', 'get').inc(1)
    # counter.labels('success', 'get').set_to_current_time() # just for gauge
    pushadd_to_gateway('http://arz.local:9191',
                       job='batchA', registry=registry)


if __name__ == '__main__':
    def sync_main():
        try:
            set_interval(function=func, interval=1)
        except Exception:
            raise RuntimeError("Exception's Sync loop")
    sync_main()
