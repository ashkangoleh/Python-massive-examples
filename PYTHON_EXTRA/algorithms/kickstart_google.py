"""
Problem 
    There are 'N' house for sale. The o-th hose cost A dollars to buy. You have a budget off B dollars to spend.

    What is the maximum number of houses you can buy?

Input
    The first line of the input gives the number of test cases, T. T test cases follow, Each test case begins with a single line containing the two integers 
    N and B the second line contains N integers. The i-th integer is A, the cost of the i-th house.

Output
    for each test case, output one line containing Case #x: y, where x is the test case number(starting from 1) and y is the maximum number of houses you can buy.
    
Limits 
    time limit: 15seconds per test set.
    memory limit: 1GB.
    1 <= T <= 100
    1 <= B <= 10**5
    1 <= A <= 1000, for all i.
"""


t = int(input())
for x in range(1, t+1):
    n, b = map(int, input().split())
    houses = list(map(int, input().split()))
    houses.sort()
    y = 0
    for house in houses:
        if b >= house:
            b -= house
            y += 1

        else:
            break

    print("Case #%s: %s" % (x, y))
