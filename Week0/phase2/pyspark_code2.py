from pyspark.sql import SparkSession
from pyspark.sql.functions import count, sum, avg

spark = SparkSession.builder.appName("Praveen").getOrCreate()

# Customers table
customers_data = [
    (1, "Ravi", "Hyderabad"),
    (2, "Sita", "Chennai"),
    (3, "Arun", "Bangalore"),
    (4, "Priya", "Hyderabad"),
    (5, "Kiran", "Mumbai")
]

customers = spark.createDataFrame(customers_data, ["customer_id", "name", "city"])

# Orders table
orders_data = [
    (101, 1, 500),
    (102, 1, 300),
    (103, 2, 700),
    (104, 3, 200),
    (105, 3, 400),
    (106, 4, 1000)
]

orders = spark.createDataFrame(orders_data, ["order_id", "customer_id", "amount"])

customers.show()
orders.show()

customers = customers.dropna(subset=["customer_id"])
orders = orders.dropna(subset=["customer_id"])

orders.groupBy("customer_id") \
    .agg(sum("amount").alias("total_amount")) \
    .show()

orders.groupBy("customer_id") \
    .agg(sum("amount").alias("total_amount")) \
    .orderBy("total_amount", ascending=False) \
    .limit(3) \
    .show()

customers.join(orders, "customer_id", "left") \
    .filter(orders.customer_id.isNull()) \
    .select(customers.customer_id) \
    .show()

customers.join(orders, "customer_id") \
    .groupBy("city") \
    .agg(sum("amount").alias("total_revenue")) \
    .show()

orders.groupBy("customer_id") \
    .agg(avg("amount").alias("avg_amount")) \
    .show()

orders.groupBy("customer_id") \
    .agg(count("*").alias("order_count")) \
    .filter("order_count > 1") \
    .show()


orders.groupBy("customer_id") \
    .agg(sum("amount").alias("total_amount")) \
    .orderBy("total_amount",ascending=False) \
    .show()