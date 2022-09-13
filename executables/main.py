import random
import argparse
import time


parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-e", "--entry", type=int, help="Message", required=False)
# Read arguments from command line
args = parser.parse_args()

print("start: ", time.time())
list = []
x = args.entry

for i in range(x):
    list.append(random.randint(0, x))

print("meanwhile: ", time.time())
iteration_li = iter(list)
print(sum(iteration_li))
print("end: ", time.time())
