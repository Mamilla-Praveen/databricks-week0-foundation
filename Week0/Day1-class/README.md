# README – Day 1: Introduction to PySpark, Databricks & Data Cleaning

# Topic Covered
Introduction to PySpark, overview of Databricks platform, SparkSession setup, loading CSV data, basic data exploration, and data cleaning techniques including handling null values.

# Objective
The main objective of this session was to understand the fundamentals of PySpark and the Databricks environment. By the end of this session, we learned how to initialize Spark, work in Databricks notebooks, load data, explore datasets, and handle missing values effectively.

# Introduction to Databricks
Databricks is a cloud-based platform used for big data processing and analytics. It provides an interactive workspace where we can write PySpark code in notebooks and execute it easily.

Key features of Databricks:
- Notebook-based environment (similar to Jupyter)
- Supports multiple languages (Python, SQL, Scala)
- Built-in Apache Spark support
- Easy data visualization and execution
- Cluster-based computing for large-scale data

# Environment Setup
In Databricks, SparkSession is automatically created. However, in a normal environment, we initialize it manually.

from pyspark.sql import SparkSession  
spark = SparkSession.builder.appName("Day1_Practice").getOrCreate()

# Loading Data
We loaded the dataset using the CSV reader with header option enabled so that column names are automatically detected.

df = spark.read.option("header", "true").csv("path/to/file.csv")

# Data Exploration
We explored the dataset using different PySpark functions to understand its structure and contents.

df.show() – Displays the data  
df.printSchema() – Shows column data types  
df.describe().show() – Provides summary statistics  
df.columns – Lists all column names  
df.count() – Returns total number of rows  

# Data Cleaning
Data cleaning is an important step before performing any analysis. We focused on handling missing or null values.

# Handling Null Values

# Drop Null Rows
Used to remove rows that contain null values in any column.

df.dropna()

# Drop Nulls Based on Specific Columns
Removes rows only when null values are present in specified columns.

df.dropna(subset=["column_name"])

# Fill Null Values
Replaces null values with a specific value.

df.fillna({"column_name": 0})

# Fill Multiple Columns
Used to replace null values in multiple columns at once.

df.fillna({
    "age": 0,
    "city": "Unknown"
})

# Drop Rows with All Null Values
Removes rows where all columns contain null values.

df.dropna(how="all")

# Drop Based on Threshold
Keeps rows that have a minimum number of non-null values.

df.dropna(thresh=2)

# Column Operations
Basic column operations were also practiced.

df.select("column1", "column2")  
df.withColumnRenamed("old_name", "new_name")  
df.drop("column_name")  

# Common Errors
Some common issues encountered during practice:

spark is not defined – occurs when SparkSession is not initialized  
Incorrect file path – ensure correct dataset location  
Confusion between dropna and fillna – one removes data, the other replaces it  

# Key Learnings
Databricks provides an easy environment to run PySpark code  
PySpark is used for handling large-scale data processing  
SparkSession is required to start working with PySpark  
DataFrames are similar to tables in SQL  
Handling null values is crucial for accurate analysis  
dropna removes rows while fillna replaces missing values  

# Practice Tasks
Load a dataset in Databricks and explore its schema  
Count total number of rows  
Identify and handle null values  
Drop rows with null values  
Replace null values using fillna  
Perform column operations like rename and select  

# Conclusion
Day 1 focused on building a strong foundation in PySpark and understanding the Databricks platform. We learned how to work with DataFrames, explore datasets, and handle missing data effectively, which is essential for real-world data processing.
