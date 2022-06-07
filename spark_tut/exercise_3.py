from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("Python Spark DataFrames basic example").getOrCreate()
df = spark.read.json("people.json").cache()
print('df: ', df)