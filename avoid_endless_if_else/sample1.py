def do_one(x):
    print("one: x*1=", x*1)


def do_two(x):
    print("two: x*2=", x*2)


def do_three(x):
    print("three: x*3=", x*3)


def do_four(x):
    print("four: x*4=", x*4)


def do_default(x):
    print("default: x=", x)


x = 3

if x==1:
    do_one(x)
elif x==2:
    do_two(x)
elif x==3:
    do_three(x)
elif x==4:
    do_four(x)
else:
    do_default(x)
    
    
# avoid endless if else
actions = {
    1:do_one,
    2:do_two,
    3:do_three,
    4:do_four
}
action = actions.get(x,do_default)
action(x)
