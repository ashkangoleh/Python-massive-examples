def bubble_sort(ourlist):  # I create my function bubble_sort with the argument called ourlist
    b = len(ourlist)  # for every list, I will have a minus 1 iteration
    swapped = False
    # for each element in the range of b, I check if they are ordered or not
    for x in range(b-1, 0, -1):
        for y in range(x):
            # if one element is greater than the nearest element in the list
            if ourlist[y] > ourlist[y+1]:
                swapped = True
                # I have to swap the element, in other words
                ourlist[y], ourlist[y+1] = ourlist[y+1], ourlist[y]
                # I exchange the position of the two elements
        if not swapped:
            return ourlist

# def bubble_sort(elements):
#     swapped = False
#     for n in range(len(elements) - 1, 0, -1):
#         for i in range(n):
#             if elements[i] > elements[i+1]:
#                 swapped = True
#                 elements[i], elements[i+1] = elements[i+1], elements[i]
#         if not swapped:
#             return


ourlist = [15, 1, 9, 3]
bubble_sort(ourlist)
print("==>> ourlist: ", ourlist)


def old_school_bubble_sort(elements):
    do = 0
    while not do:
        do = 1
        for n in range(1, len(elements)):
            # left to right
            if elements[n-1] > elements[n]:
                elements[n-1], elements[n] = elements[n], elements[n-1]
                do = 0
    print(elements)
    return elements

old_school_bubble_sort([4, 7, 1, 6, 5, 10, 50, 60, 70, 32, 0, 42, 35, -20, -1])
