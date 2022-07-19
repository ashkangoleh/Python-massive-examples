fruits = ["apple", "orange", "pear", "pineapple"]
prices = [4, 5, 6, 7]

result = {}
for f,p in zip(fruits,prices):
    result[f] = p
    
print(result)
