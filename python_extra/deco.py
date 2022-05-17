import time


# def tracer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         return_value = func(*args, **kwargs)
#         end = time.time()
#         print(f"Elapsed:{end-start}")
#         return return_value
#     return wrapper


# @tracer
# def main(name: str) -> print:
#     print(f"Hello {name}")
#     # return f"Hello {name}"


# # print('hello.__name__: ', hello.__name__)

# # print(main("ashkan"))
# main("Ashkan")

def int_inputs(prefix):
    def none_zero(func):
        def wrapper(*args, **kwargs):
            newargs = [int(a) for a in args]
            if prefix in newargs:
                raise f"{newargs} not allowed"
            else:
                return func(*newargs)
        return wrapper
    return none_zero


@int_inputs(0)
def add(a,b):
    return a+b


print(add(0,0))