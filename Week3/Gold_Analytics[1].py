# Databricks notebook source
df_sales = spark.table("`e-commerce_sales_catalog`.silver.silver_sales_detail")

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI 1: Daily Revenue

# COMMAND ----------

from pyspark.sql.functions import *

df_daily_revenue = df_sales.withColumn(
    "order_date",
    to_date(col("order_purchase_timestamp"))
).groupBy("order_date").agg(
    sum("total_amount").alias("daily_revenue")
)

# COMMAND ----------

df_daily_revenue.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.gold.gold_daily_revenue")

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI 2: Top Customers per city

# COMMAND ----------

from pyspark.sql.functions import sum

df_top_customers = df_sales.groupBy(
    "customer_id", "customer_city"
).agg(
    sum("total_amount").alias("total_spent")
)

# COMMAND ----------

from pyspark.sql.window import Window
from pyspark.sql.functions import rank, col

df_top_customers = df_top_customers.repartition("customer_city")

window_spec = Window.partitionBy("customer_city") \
                    .orderBy(col("total_spent").desc())

df_top_customers = df_top_customers.withColumn(
    "rank",
    rank().over(window_spec)
)

# COMMAND ----------

df_top_customers.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.gold.gold_top_customers")

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI 3: Top Products

# COMMAND ----------

df_top_products = df_sales.groupBy(
    "product_id", "product_category_name"
).agg(
    sum("total_amount").alias("revenue")
)

# COMMAND ----------

df_top_products.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.gold.gold_top_products")

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI 4: Category Performance

# COMMAND ----------

df_category = df_sales.groupBy(
    "product_category_name"
).agg(
    sum("total_amount").alias("total_revenue")
)

# COMMAND ----------

df_category.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.gold.gold_category_performance")

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI 5: Monthly Revenue Trend

# COMMAND ----------

from pyspark.sql.functions import *

df_monthly = df_sales.withColumn(
    "year", year(col("order_purchase_timestamp"))
).withColumn(
    "month", month(col("order_purchase_timestamp"))
).groupBy("year", "month").agg(
    round(sum("total_amount"), 2).alias("monthly_revenue")
)

# COMMAND ----------

df_monthly.show()

# COMMAND ----------

# DBTITLE 1,Cell 17
df_monthly = df_monthly.orderBy("year", "month")

# COMMAND ----------

df_monthly.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("`e-commerce_sales_catalog`.gold.gold_monthly_revenue")

# COMMAND ----------

spark.table("`e-commerce_sales_catalog`.gold.gold_monthly_revenue").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ### KPI 6: Delivery Time Analysis

# COMMAND ----------

from pyspark.sql.functions import *

df_delivery = df_sales.withColumn(
    "delivery_days",
    datediff(col("order_delivered_customer_date"), col("order_purchase_timestamp"))
)

# COMMAND ----------

df_delivery_kpi = df_delivery.groupBy().agg(
    round(avg("delivery_days"), 2).alias("avg_delivery_days")
)

# COMMAND ----------

df_delivery_kpi.show()

# COMMAND ----------

