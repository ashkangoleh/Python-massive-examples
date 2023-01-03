from functools import wraps
from typing import Callable


def repeat(number: int, message: str):
    """Repeat function call x amount of times"""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = None
            for _ in range(number):
                value = func(*args, **kwargs)
            print(message)
            return value
        return wrapper
    return decorator


@repeat(3, 'Done!')
def func1():
    print("Ashkan")


if __name__ == "__main__":
    func1()
