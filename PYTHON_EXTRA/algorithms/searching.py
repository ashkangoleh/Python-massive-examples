def lin_search(ourlist, key):
    
    for index in range(0, len(ourlist)):
        if (ourlist[index] == key):
            return  index
    else:
        return "not fund"
    
ourlist = [15, 1, 9, 3]

print("==>> index 9 is: ", lin_search(ourlist, 9))
