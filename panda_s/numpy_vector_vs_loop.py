import numpy as np
import time


list1 = np.random.rand(100)
list2 = np.random.rand(100)

start = time.time()
result = list1 * list2
end = time.time()

print("time for element-wise multiplication using vectorization: ", end - start)


result2 = []
start = time.time()
for item in range(len(list1)):
    result2.append(list1[item]*list2[item])
end = time.time()
print("time for element-wise multiplication using loop: ", end - start)

if list(result) == result2:
    print("both are equal")
else:
    print("both are different")
    

