# README – Day 2: SQL Joins & Important Query Concepts

# Topic Covered
Understanding SQL joins, combining data from multiple tables, and solving important SQL queries used in real-world data analysis and interview scenarios.

# Objective
The objective of this session was to learn how to connect multiple tables using joins and apply SQL concepts to solve different types of analytical queries.

# Introduction to Joins
Joins are used to combine data from two or more tables based on a common column. They help in extracting meaningful insights by linking related datasets.

# Types of Joins

# INNER JOIN
Returns only the records that have matching values in both tables. Non-matching records are excluded.

# LEFT JOIN
Returns all records from the left table and matching records from the right table. If no match exists, NULL values are returned for the right side.

# RIGHT JOIN
Returns all records from the right table and matching records from the left table. If no match exists, NULL values are returned for the left side.

# FULL JOIN
Returns all records from both tables. Non-matching rows from either side are filled with NULL values.

# CROSS JOIN
Returns all possible combinations of rows from both tables, creating a cartesian product.

# SELF JOIN
A table joined with itself, useful for hierarchical data such as employee-manager relationships.

# Important SQL Concepts

# GROUP BY
Used to group similar rows together, mainly for performing aggregate calculations.

# Aggregate Functions
Functions such as SUM, COUNT, AVG, MIN, and MAX are used to perform calculations on grouped data.

# HAVING
Used to filter grouped data after aggregation.

# ORDER BY
Used to sort data in ascending or descending order.

# WHERE
Used to filter data before applying grouping or aggregation.

# CASE Statement
Used to apply conditional logic in SQL, similar to if-else statements.

# NULL Handling
Understanding how NULL values behave in joins and conditions is essential for accurate query results.

# Queries Solved During Practice
During this session, multiple practical queries were solved to strengthen understanding:

- Calculating total orders and total sales per customer  
- Finding top customers based on total spending  
- Identifying customers with no orders using joins  
- Calculating average, minimum, and maximum values  
- Performing city-wise or category-wise aggregations  
- Finding records based on conditions and filtering  
- Sorting data based on different columns  
- Using conditional logic to categorize data  
- Identifying duplicate and unique records  
- Working with grouped data using HAVING conditions  

# Common Errors
Using incorrect join conditions  
Forgetting to include ON clause  
Confusing LEFT JOIN with INNER JOIN  
Not handling NULL values properly  
Using WHERE instead of HAVING for aggregated data  

# Key Learnings
Joins help combine data from multiple tables  
Different joins are used based on requirements  
GROUP BY is used for aggregation  
HAVING is used to filter aggregated data  
Understanding NULL values is important in joins  
SQL queries can be used to derive meaningful insights from raw data  

# Practice Tasks
Understand and differentiate all types of joins  
Solve aggregation-based queries  
Practice filtering and sorting data  
Work on real-world query scenarios  
Apply conditional logic using CASE statements  

# Conclusion
Day 2 focused on SQL joins and solving practical queries. This session helped in building strong problem-solving skills using SQL, which are essential for data analysis.
