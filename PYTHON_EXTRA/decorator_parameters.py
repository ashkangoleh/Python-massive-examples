from functools import reduce

def repetition_fibo(repetition):
    def decorator(func):
        def wrapper(type:str=None):
            #type 's' means series
            if type == 's':
                for i in range(repetition):
                    fib = lambda n: reduce(lambda x,n:[x[1],x[0]+x[1]],range(i),[0,1])
                    current_step = fib(i)[0]
                    next_step = fib(i)[1]
                    print(f'fib=>{i} =', list((f'{i}-> {current_step}',f'next number({i+1})-> fibo number: {next_step}')))
            else:
                fib = lambda n: reduce(lambda x,n:[x[1],x[0]+x[1]],range(repetition),[0,1])
                current_step = fib(repetition)[0]
                next_step = fib(repetition)[1]
                print(f'fib=>{repetition} =', list((current_step,f'next({repetition+1})-> fibo number: {next_step}')))
        return wrapper
    return decorator



def fibonacci_generator(type:str=None,num:int=0):
    @repetition_fibo(num)
    def func(type:str=None):
        return
    func(type).__repr__()


fibonacci_generator(type='s',num=100)