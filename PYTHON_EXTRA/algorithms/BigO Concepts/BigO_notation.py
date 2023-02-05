# Big O notation is a way of describing the performance or complexity of an algorithm. It provides an upper bound on the growth rate of the number of operations required by an algorithm as a function of the size of the input data. It helps to evaluate the efficiency of an algorithm and to compare different algorithms by their running time and memory usage.

# Big O notation uses a set of standard notations, such as O(1), O(n), O(n^2), O(log n), O(n log n), etc. Here, n represents the size of the input data.

# O(1) means that the number of operations is constant and does not depend on the size of the input data.
# O(n) means that the number of operations grows linearly with the size of the input data.
# O(n^2) means that the number of operations grows quadratically with the size of the input data.
# O(log n) means that the number of operations grows logarithmically with the size of the input data.
# O(n log n) means that the number of operations grows in the order of n log n with the size of the input data.


#-------> O(1):
# returning the first element of a list
def first_element(arr):
    return arr[0]

# The time complexity of this algorithm is O(1), 
# since the number of operations is constant and does not depend on the size of the input data (arr).


#-------> O(n):
# Linear search algorithm
# finding the maximum element in a list
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# The time complexity of this algorithm is O(n), 
# since the number of operations grows linearly with the size of the input data (arr).

#-------> O(n^2):
# Bubble sort algorithm
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

#-------> O(log n):
# Binary search algorithm
def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#-------> O(n log n):
# Merge sort algorithm
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

