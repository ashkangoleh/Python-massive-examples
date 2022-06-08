from pyspark.sql import SparkSession
# Creating a spark session
spark = SparkSession.builder.master("local").appName("Python Spark DataFrames basic example").getOrCreate()
# Read the dataset into a spark dataframe using the `read.json()` function
df = spark.read.json("/drive_data/test_proj/spark_tut/people.json").cache()
# Print the dataframe as well as the data schema
df.show()
df.printSchema()
# Register the DataFrame as a SQL temporary view
df.createTempView("people")

# Select and show basic data columns
df.select("name").show()
df.select("age").show()
spark.sql("SELECT name FROM people").show()


#Perform basic filtering
df.filter(df['age'] > 21).show()

spark.sql("SELECT name,age from people where age > 21;").show()


