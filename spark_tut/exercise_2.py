import time
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# Creating a spark context class
sc = SparkContext()


data = range(1, 30)
# print first element of iterator
print(data[0])
len(data)
xrangeRDD = sc.parallelize(data, 4)

# this will let us know that we created an RDD
print('xrangeRDD: ', xrangeRDD)
print("*"*80)

# Transformations
subRDD = xrangeRDD.map(lambda x: x-1)
print('subRDD: ', subRDD)
filteredRDD = subRDD.filter(lambda x: x < 10)
print('filteredRDD: ', filteredRDD, end="\n")
print("*"*80)

print('subRDD(collect): ', subRDD.collect())
print('filteredRDD(collect): ', filteredRDD.collect())
print('filteredRDD(count): ', filteredRDD.count())
print("*"*80)

# Distribute a local Python collection to form an RDD. Using range is recommended if the input represents a range for performance.
listRDD = sc.parallelize([1, 2, 3, 4, 5, 6], 7).glom().collect()
print('listRDD: ', listRDD)
print("*"*80)

# Caching Data
# This simple example shows how to create an RDD and cache it. Notice the 10x speed improvement! If you wish to see the actual computation time, browse to the Spark UI...it's at host:4040. You'll see that the second calculation took much less time!


test = sc.parallelize(range(1, 50000), 4)
test.cache()

t1 = time.time()
# first count will trigger evaluation of count *and* cache
count1 = test.count()
print('count1: ', count1)
dt1 = time.time() - t1
print("dt1: ", dt1)


t2 = time.time()
# second count operates on cached data only
count2 = test.count()
print('count2: ', count2)
dt2 = time.time() - t2
print("dt2: ", dt2)

test.count()


# time.sleep(3600)
