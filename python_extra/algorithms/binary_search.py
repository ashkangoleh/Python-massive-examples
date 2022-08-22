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
