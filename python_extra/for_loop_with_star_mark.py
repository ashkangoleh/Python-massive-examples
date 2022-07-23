
w = list(map(lambda x: x**2, [i for i in range(3)]))
e = ("hello world",)


e1 = "hello world"
if m := len(e1) > 0 :
    print("==>> e1: ", *e1[3])
else:
    print("<>")
# `*e1` is like loop in python

e2 = {"hello_world": "123"}


print(list(*e2.values()).__repr__())
