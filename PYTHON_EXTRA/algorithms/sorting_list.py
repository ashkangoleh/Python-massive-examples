li = [8, 10, 6, 2, 4,1]  # list to sort

def sorting_list(li)->list:
    swapped = True  # It's a little fake, we need it to enter the while loop.

    while swapped:
        swapped = False  # no swaps so far
        for i in range(len(li)-1):
            if li[i] > li[i+1]:
                swapped = True  # a swap occurred!
                li[i], li[i+1] = li[i+1], li[i]
    return li


print("==>> sorting_list(li): ", sorting_list(li))


