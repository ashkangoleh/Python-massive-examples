def binary_search(orderList, key):
    low = 0
    high = len(orderList) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2

        print("==>> orderList[mid]: ", orderList[mid])
        if orderList[mid] < key:
            low = mid + 1
            print("==>> low: ", low)

        elif orderList[mid] > key:
            high = mid - 1
            print("==>> high: ", high)
        else:
            return True, f"index of {key} is {mid}"
    return False, f"{-1} not found ! !"


# print("==>> binary_search([1, 3, 9, 15, 17], 19): ",
#       binary_search([1, 3, 9, 15, 17], 19))
print("==>> binary_search([1, 3, 9, 15], 9): ",
      binary_search([1, 3, 9, 15], 9))


def binarySearch(inlist, key):
    left = 0
    right = len(inlist) - 1
    mid = 0

    while left <= right:
        mid = (left+right) // 2

        if inlist[mid] < key:
            left = mid + 1
        elif inlist[mid] > key:
            right = mid - 1
        else:
            return True
    return False

print("==>> binary_search([1, 3, 9, 15], 9): ",
      binarySearch([1, 3, 9, 15], 9))