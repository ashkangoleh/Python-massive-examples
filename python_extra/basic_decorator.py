import time
def decorator(anything):
    def wrapper():
        print("decoration begins")
        #if object passed as function we call it otherwise do what ever we want
        anything()
        print("decoration ends")
    return wrapper

def func():
    print("none decoration functions")

###we are capturing decorator as new_func here
new_func = decorator(func)
new_func()

###we are overwritting function name here 
func = decorator(func) #(I)
func()

###we using decorator here
@decorator #-> works same as (I)
def func():
    print("none decoration functions")
    
func()

def duration_decorator(anything):
    def wrapper():
        start_time = time.time()
        print('start_time ', start_time)
        anything()
        end_time = time.time() - start_time
        print(f'duration {end_time:5f}')
    return wrapper
#### if duration decorator be top of decorator it'll run first then decorator like
'''
    start_time  1652084789.9146717
    decoration begins
    none decoration functions
    decoration ends
    duration 1.001113
'''
#### if duration decorator be below of decorator it'll run after decorator like
'''
    decoration begins
    start_time  1652084881.2876134
    none decoration functions
    duration 1.000596
    decoration ends
'''
@decorator #-> works same as (I)
@duration_decorator
def func():
    print("none decoration functions")
    time.sleep(1)
    
func()



def double_decorator(anything):
    def wrapper():
        anything()
        anything()
    return wrapper

@double_decorator
@decorator #-> works same as (I)
@duration_decorator
def func():
    print("none decoration functions")
    time.sleep(1)
    
func()
