from pyspark.sql import SparkSession
from pyspark.sql.functions import col,count

spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

data = [
(1, "Ravi", "Hyderabad", 25),
(2, None, "Chennai", 32),
(None, "Arun", "Hyderabad", 28),
(4, "Meena", None, 30),
(4, "Meena", None, 30),
(5, "John", "Bangalore", -5)
]

columns = ["customer_id", "name", "city", "age"]

df = spark.createDataFrame(data, columns)
df.show()


# Null values
# df.select([count(col(c)).alias(c) for c in df.columns]).show()

# Rows with nulls
df.filter(
    col("customer_id").isNull() |
    col("name").isNull() |
    col("city").isNull() |
    col("age").isNull()
).show()


# Duplicate rows
df.groupBy(*df.columns).count().filter("count > 1").show()

# Invalid age (negative)
df.filter(col("age") < 0).show()



df_clean = df.filter(col("customer_id").isNotNull())



df_clean = df_clean.fillna({
    "name": "Unknown",
    "city": "Unknown"
})


df_clean = df_clean.dropDuplicates()

df_clean = df_clean.filter(col("age") > 0)


print("Before cleaning:", df.count())
print("After cleaning:", df_clean.count())


df_clean.groupBy("city").count().show()