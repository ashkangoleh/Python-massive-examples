def decorator(func):
    def wrapper(*args, **kwargs):
        print("Start")
        func(*args, **kwargs)
        print("End")
    return wrapper

@decorator
def func(func_parameters):
    print(func_parameters)
    


func("somthings cool")
