import sys
"""
$python main.py
# error happens here
Error happened! : error message here
"""


def catches(catch):
    """
    catch is a tuple of exceptions, like (TypeError, RuntimeError)
    """
    def decorator(func):
        
        def newFunc(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except catch as e:
                print(f"caught an error: {repr(e)}")
        return newFunc
    return decorator
    

@catches((RuntimeError,TypeError))
def main(arguments):
    if len(arguments)>1:
        print("we have some arguments")
        print(f"{arguments}")
    else:
        raise RuntimeError("no arguments passed in!")
@catches((RuntimeError,ValueError))
def add_argument(l1:int=None,l2:int=None)-> int:
    try:
        if (l1 and l2) is not None:
            print(l1 + l2)
        else:
            raise ValueError("no arguments passed in!")
    except RuntimeError as e:
        return ValueError("no arguments passed in!")
if __name__ == "__main__":
    main(sys.argv)
    if sys.argv.__len__() > 1:
        l1 = int(sys.argv[1])
        l2 = int(sys.argv[2])
        add_argument(l1,l2)
    add_argument()