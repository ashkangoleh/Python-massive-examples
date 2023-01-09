import asyncio
import threading
from typing import Optional, Union
from prometheus_client import CollectorRegistry, Gauge, Counter, pushadd_to_gateway


registry = CollectorRegistry()

counter = Counter(
    name="its_name_for_metrics",
    documentation="its help for counter tracking",
    labelnames=['status', 'method'],
    registry=registry
)


def set_interval(function: callable, interval: int, _async: Optional[bool], obj: Union[str, int, dict, None] = None):
    def _wrapper():
        if _async:
            loop = asyncio.new_event_loop()
            set_interval(function, interval, _async, obj)
            loop.run_until_complete(function(obj))
        else:
            set_interval(function, interval, _async, obj)
            function(obj)

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
            set_interval(function=func, interval=1, _async=False, obj=None)
        except Exception:
            raise RuntimeError("Exception's Sync loop")
    sync_main()
