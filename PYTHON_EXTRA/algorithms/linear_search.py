def linear_search(values, search_for):
    search_at = 0
    search_res = False

    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at += 1
    return search_res


l = [1, 0, 2, 5, 200, 150, 657, 321, 12, 78,10]
print(linear_search(l, 10))
# print(linear_search(l, 90))
