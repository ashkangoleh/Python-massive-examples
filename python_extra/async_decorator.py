"""
    Asynchronous execution as a decorator
    Author : AshkanGolehPour
    date : Saturday 3 September 09:29 LocalTime
"""
import asyncio


def async_run(coroutine):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        try:
            return loop.run_until_complete(coroutine(*args, **kwargs))
        finally:
            loop.close()
    return wrapper



@async_run
async def main():
    print("Asynchronous function calling with decorator")
    return 1

if __name__ == "__main__":
    main()

