# Phase 2 – Data Transformation using PySpark

## Objective

The objective of this phase is to perform data transformations on the given datasets using PySpark. This includes joining multiple datasets, applying aggregations, and generating meaningful business insights from the data.

---

## Problem Summary

In this phase, I worked with multiple datasets such as:

* Customers
* Orders

The main tasks were:

* Combine data from different tables
* Perform aggregations on transactional data
* Extract useful insights for analysis

---

## Approach

The following steps were followed to complete the task:

1. Loaded datasets into PySpark DataFrames
2. Performed basic data cleaning:

   * Removed null values where necessary
   * Ensured correct data types for columns
3. Joined multiple tables using appropriate keys
4. Applied transformations:

   * Used `groupBy()` and aggregation functions
   * Applied filtering conditions
5. Generated final result datasets for analysis

---

## Key Transformations Used

* `join()` → To combine multiple datasets
* `groupBy()` → To group data for aggregation
* `agg()` → To compute metrics like sum, count, and average
* `filter()` → To remove unwanted or irrelevant data

---

## Output / Results

The following outputs were generated:

* Aggregated customer-level data
* Summary metrics from transactional datasets

Screenshots of outputs are available in the `outputs2/` folder.

---

## Data Engineering Considerations

* Handled null values to avoid incorrect aggregations
* Ensured joins did not create duplicate records
* Verified outputs using sample data checks

---

## Challenges Faced

* Understanding correct join conditions between tables
* Handling missing or null values in datasets

---

## Learnings

* Learned how to perform joins in PySpark
* Understood the importance of data cleaning before transformations
* Gained knowledge of aggregation techniques used in real-world data engineering

---

## Files in this Folder

* `pyspark_code2.py` → PySpark implementation
* `sql_queries2.sql` → SQL queries for the same tasks
* `outputs2.zip` → Output screenshots

---

## Conclusion

This phase helped me bridge the gap between SQL and PySpark by applying real-world data transformation techniques. It strengthened my understanding of joins, aggregations, and data processing workflows used in data engineering.

---
