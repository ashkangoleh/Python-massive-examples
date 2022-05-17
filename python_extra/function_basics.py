def func():
    print('Function: ', 'Function')

def wrapper(function):
    print('function: type->', function,'')
    #run function inside func , its depends on () if we want call the func from outside of this function
    function()
    print('function: GoodBye')

def function_generator():
    #[
    def new_function():
        print('New Function: ', 'new_function()')
    #]
    return new_function

wrapper(func)
 

new_func= function_generator()
new_func() 
