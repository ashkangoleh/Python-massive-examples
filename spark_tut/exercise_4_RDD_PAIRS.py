from logging import warning
from pyspark import SparkContext
from pyspark.sql import SparkSession
import os

cwd = os.path.dirname(__file__)
# Creating a spark context class
sc = SparkContext()
# Creating a spark session
spark = SparkSession.builder.master("local").appName(
    "Python Spark DataFrames basic example").getOrCreate()

print("*"*100, end="\n")
# load json file
json_file_path = spark.read.json(f"{cwd}/people.json").cache()
print('json_file_path: ', json_file_path)
print("*"*100, end="\n")
# load file text (create a baseRDD from file path)
file_path = sc.textFile("{cwd}/README.md")
print('file_path: ', file_path)
print("*"*100, end="\n")
# load list
numb = range(1, 100)
load_numbers = sc.parallelize(numb)
print('load_numbers: ', load_numbers.collect())
print("*"*100, end="\n")

# function programming
numRDD = sc.parallelize([1, 2, 3, 4])
print('type(numRDD): ', type(numRDD))
print("*"*100, end="\n")
# parallelize() method
numRDD_Partitions = sc.parallelize(range(10), 7)
print('numRDD_Partitions_collect: ', numRDD_Partitions.collect())
print("*"*100, end="\n")
# glom coalescing(ادغام) all elements within each partition into list
print('numRDD_Partitions_glom_collect: ', numRDD_Partitions.glom().collect())
print('numRDD_Partitions_number: ', numRDD_Partitions.getNumPartitions())
print("*"*100, end="\n")
# Basic RDD transformations
# map() transformation

RDD = sc.parallelize([1, 2, 3, 4])
RDD_map = RDD.map(lambda x: x * x)
print('RDD_map: ', RDD_map)
print('RDD_map_first: ', RDD_map.first())
print('RDD_map_take: ', RDD_map.take(3))
print('RDD_map_count: ', RDD_map.count())
print('RDD_map_collect: ', RDD_map.collect())
print('RDD_map_glom_collect: ', RDD_map.glom().collect())
print("*"*100, end="\n")
# filter()
RDD_filter = RDD.filter(lambda x: x > 2)
print('RDD_filter: ', RDD_filter)
print('RDD_filter_first: ', RDD_filter.first())
print('RDD_filter_take: ', RDD_filter.take(3))
print('RDD_filter_count: ', RDD_filter.count())
print('RDD_filter_collect: ', RDD_filter.collect())
print('RDD_filter_glom_collect: ', RDD_filter.glom().collect())


print("*"*100, end="\n")
# flatMap()
RDD_text = sc.parallelize(["hello world", "how are you"])
RDD_flatMap = RDD_text.flatMap(lambda x: x.split(" "))
print('RDD_flatMap: ', RDD_flatMap)
print('RDD_flatMap_first: ', RDD_flatMap.first())
print('RDD_flatMap_take: ', RDD_flatMap.take(3))
print('RDD_flatMap_count: ', RDD_flatMap.count())
print('RDD_flatMap_collect: ', RDD_flatMap.collect())
print('RDD_flatMap_glom_collect: ', RDD_flatMap.glom().collect())
print("*"*100, end="\n")

# Union()
inputRDD = sc.textFile(f"{cwd}/logs.txt", minPartitions=6)
errorRDD = inputRDD.filter(lambda x: "ERROR" in x.split())
warningRDD = inputRDD.filter(lambda x: "WARNING" in x.split())
combinedRDD = errorRDD.union(warningRDD)
print('combinedRDD: ', combinedRDD)
print('combinedRDD_first: ', combinedRDD.first())
print('combinedRDD_take: ', combinedRDD.take(3))
print('combinedRDD_count: ', combinedRDD.count())
print('combinedRDD_collect: ', combinedRDD.collect())
print('combinedRDD_glom_collect: ', combinedRDD.glom().collect())
print("*"*100, end="\n")

# creating pair RDDs
my_tuple = [("sam", 23), ("mary", 34), ("peter", 25)]
pairRDD_tuple = sc.parallelize(my_tuple)
print('pairRDD_tuple: ', pairRDD_tuple)
print('pairRDD_tuple_collect: ', pairRDD_tuple.collect())
print("*"*50, end="\n")
my_list = ["sam 23", "mary 34", "peter 25"]
regularRDD = sc.parallelize(my_list)
pairRDD_list = regularRDD.map(lambda s: (s.split(' ')[0], s.split(' ')[1]))
print('pairRDD_list: ', pairRDD_list)
print('pairRDD_list_count: ', pairRDD_list.collect())
print("*"*100, end="\n")


# examples of paired RDD transformations
# reduceByKey(func) combine values with the same key
# groupByKey() group values with same key
# sortByKey() Return on RDD sorted by the key
# join() join two pair RDDs based on their key


# reduceByKey(func)
regularRDD_2 = sc.parallelize(
    [("messi", 23), ("ronaldo", 34), ("neymar", 22), ("messi", 24)])
pairRDD_reducebykey = regularRDD_2.reduceByKey(lambda x, y: x + y)
print('pairRDD_reducebykey: ', pairRDD_reducebykey.collect())
print("*"*50, end="\n")

# sortByKey()
pairRDD_reducebykey_rev = pairRDD_reducebykey.map(lambda x: (x[1], x[0]))
print('pairRDD_reducebykey_rev(desc): ',
      pairRDD_reducebykey_rev.sortByKey(ascending=False).collect())
print('pairRDD_reducebykey_rev(asc): ',
      pairRDD_reducebykey_rev.sortByKey(ascending=True).collect())
print("*"*50, end="\n")

# groupByKey()
airports = [("US", "JFK"), ("UK", "LHR"), ("FR", "CDG"), ("US", "SFO")]
regularRDD_3 = sc.parallelize(airports)
pairRDD_group = regularRDD_3.groupByKey().collect()
for cont, air in pairRDD_group:
    print(f"country: {cont} , airports: {list(air)}")

print("*"*50, end="\n")

# join()
RDD1 = sc.parallelize([("messi", 34), ("ronaldo", 32), ("neymar", 24)])
RDD2 = sc.parallelize([("ronaldo", 80), ("neymar", 120), ("messi", 100)])
join_l_to_r = RDD1.join(RDD2)
# join_l_to_r:  [('ronaldo', (32, 80)), ('neymar', (22, 120)), ('messi', (34, 100))]
print('join_l(rdd1)_to_r(rdd2): ', join_l_to_r.collect())
join_r_to_l = RDD2.join(RDD1)
# join_l_to_r:  [('ronaldo', (80, 32)), ('neymar', (120, 24)), ('messi', (100, 34))]
print('join_l(rdd2)_to_r(rdd1): ', join_r_to_l.collect())
print("*"*100, end="\n")


# Advanced RDD actions

# reduce()
x = [1, 2, 3, 4]
RDD_x = sc.parallelize(x,4)
print('RDD_x: ', RDD_x.reduce(lambda x, y: x + y))

# saveAsTextFile()
RDD_x.saveAsTextFile(f"{cwd}/saveAsTextFile1.txt") # partitioned file

# coalesce()
RDD_x.coalesce(1).saveAsTextFile(f"{cwd}/saveAsTextFile2_single.txt") # single file
print("*"*100, end="\n")

###Actions operations on pair RDDs
# countByKey() only available for type(k,v)
RDD_countbykey = sc.parallelize([('a',1),('b',2),('a',1)])
print('RDD_countbykey: ', RDD_countbykey.countByKey())
for key, val in RDD_countbykey.countByKey().items():
    print(f"{key=}, {val=}")
print("*"*50, end="\n")


# collectAsMap() return the k-v pairs in the RDD as a dictionary
print(sc.parallelize([(1,2),(3,4)]).collectAsMap())
print("*"*50, end="\n")


print("*"*100, end="\n")