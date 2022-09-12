def ins_sort(ourlist):
    # loop for each element starting from 1 to the length of our list
    for x in range(1, len(ourlist)):
        k = ourlist[x]  # element with the index x
        j = x-1  # j is the index previous the index x
        # untill each element of the list are less than their previous element my loop don't stop
        while j >= 0 and k < ourlist[j]:
            # the element indexed before the element considered is set to the next one index
            ourlist[j+1] = ourlist[j]
            j -= 1  # I decrement index j by 1
        ourlist[j+1] = k  # now k is the element in the index j+1
    return ourlist


ourlist = [15, 1, 9, 3]
ins_sort(ourlist)
print("==>> ourlist: ", ourlist)
