
w = set(map(lambda x: x**2, [i for i in range(3)]))
print("==>> w: ", w)
e = ("hello world",)


e1 = "hello world"
if m := len(e1) > 0 :
    print("==>> e1: ", *e1[3])
else:
    print("<>")
# `*e1` is like loop in python

e2 = {"hello_world": "123"}


print(list(*e2.values()).__repr__())

e2 = "ashkan"
e3:list[int|str] = [
    1,2,3,4,5,6,6,7,8,9,0,"a"
]

print(*e2)
print(*e3)