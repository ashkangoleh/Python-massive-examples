def permute(list, s):
    if list == 1:
        return s
    else:
        return [
            y + x
            for y in permute(1, s)
            for x in permute(list - 1, s)
        ]


# sum all elements of a list into a single list
print(permute(2, [1, 2, 3, 4]), end=f"\n{'*'*50}\n")
print(permute(1, [1, 2, 3, 4]), end=f"\n{'*'*50}\n")

print(permute(1, ["a", "b", "c"]), end=f"\n{'*'*50}\n")
print(permute(2, ["a", "b", "c"]), end=f"\n{'*'*50}\n")
print(permute(3, ["a", "b"]), end=f"\n{'*'*50}\n")


# >>[2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]
# **************************************************
# >>[1, 2, 3, 4]
# **************************************************
# >>['a', 'b', 'c']
# **************************************************
# >>['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
# **************************************************
