from typing import Optional, Union
import threading
import asyncio


def async_run(coroutine):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coroutine(*args, **kwargs))
        finally:
            loop.close()
    return wrapper


def set_interval(function: callable, interval: int, _async: Optional[bool], obj: Union[str, int, dict]):
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


if __name__ == "__main__":
    async def custom_async_function(argument):
        print(f"{custom_async_function.__name__}_{argument*123}")

    def custom_sync_function(argument):
        print(f"{custom_sync_function.__name__}_{argument*123}")

    @async_run
    async def async_main():
        try:
            set_interval(custom_async_function, interval=1, _async=True, obj=2)
        except Exception as e:
            raise RuntimeError("Exception's Async loop")

    def sync_main():
        try:
            set_interval(custom_sync_function,
                        interval=1, _async=False, obj=2)
        except Exception as e:
            raise RuntimeError("Exception's Async loop")

    async_main()
    sync_main()
