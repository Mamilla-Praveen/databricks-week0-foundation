# Databricks notebook source
# MAGIC %md
# MAGIC ## Bronze Layer

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 1:Define the Schema

# COMMAND ----------

# DBTITLE 1,Cell 3
from pyspark.sql.types import StructType, StructField, StringType

customer_schema = StructType([
    StructField("customer_id", StringType(), True),
    StructField("customer_unique_id", StringType(), True),
    StructField("customer_zip_code_prefix", StringType(), True),
    StructField("customer_city", StringType(), True),
    StructField("customer_state", StringType(), True)
])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 2: Read CSV from Volume

# COMMAND ----------

df_customers = spark.read.format("csv") \
    .option("header", "true") \
    .schema(customer_schema) \
    .load("/Volumes/E-Commerce_Sales_Catalog/raw_files/rawdata/olist_customers_dataset.csv")


# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 3: Inspect Data

# COMMAND ----------

df_customers.printSchema()
df_customers.show(5)
print("Row Count:", df_customers.count())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 4: Add ingestion column

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

df_customers = df_customers.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Step 5: Save as Bronze Delta Table

# COMMAND ----------

df_customers.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.bronze.bronze_customers")

# COMMAND ----------

df_bronze = spark.table("bronze_customers")

df_bronze.show(5)
print("Row Count in Bronze:", df_bronze.count())

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. PRODUCTS DATASET

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType

products_schema = StructType([
    StructField("product_id", StringType(), True),
    StructField("product_category_name", StringType(), True),
    StructField("product_name_lenght", StringType(), True),
    StructField("product_description_lenght", StringType(), True),
    StructField("product_photos_qty", StringType(), True),
    StructField("product_weight_g", StringType(), True),
    StructField("product_length_cm", StringType(), True),
    StructField("product_height_cm", StringType(), True),
    StructField("product_width_cm", StringType(), True)
])

# COMMAND ----------

df_products = spark.read.format("csv") \
    .option("header", "true") \
    .schema(products_schema) \
    .load("/Volumes/e-commerce_sales_catalog/raw_files/rawdata/olist_products_dataset.csv")

# COMMAND ----------

df_products.printSchema()
print("Row Count:", df_products.count())

# COMMAND ----------

from pyspark.sql.functions import current_timestamp

df_products = df_products.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

df_products.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.bronze.bronze_products")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ORDERS DATASET

# COMMAND ----------

orders_schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("customer_id", StringType(), True),
    StructField("order_status", StringType(), True),
    StructField("order_purchase_timestamp", StringType(), True),
    StructField("order_approved_at", StringType(), True),
    StructField("order_delivered_carrier_date", StringType(), True),
    StructField("order_delivered_customer_date", StringType(), True),
    StructField("order_estimated_delivery_date", StringType(), True)
])

# COMMAND ----------

df_orders = spark.read.format("csv") \
    .option("header", "true") \
    .schema(orders_schema) \
    .load("/Volumes/e-commerce_sales_catalog/raw_files/rawdata/olist_orders_dataset.csv")

# COMMAND ----------

df_orders.printSchema()
print("Row Count:", df_orders.count())

# COMMAND ----------

df_orders = df_orders.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

df_orders.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.bronze.bronze_orders")

# COMMAND ----------

# MAGIC %md
# MAGIC ## ORDER ITEMS DATASET

# COMMAND ----------

order_items_schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("order_item_id", StringType(), True),
    StructField("product_id", StringType(), True),
    StructField("seller_id", StringType(), True),
    StructField("shipping_limit_date", StringType(), True),
    StructField("price", StringType(), True),
    StructField("freight_value", StringType(), True)
])

# COMMAND ----------

df_order_items = spark.read.format("csv") \
    .option("header", "true") \
    .schema(order_items_schema) \
    .load("/Volumes/e-commerce_sales_catalog/raw_files/rawdata/olist_order_items_dataset.csv")

# COMMAND ----------

df_order_items.printSchema()
print("Row Count:", df_order_items.count())

# COMMAND ----------

df_order_items = df_order_items.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

df_order_items.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.bronze.bronze_order_items")

# COMMAND ----------

