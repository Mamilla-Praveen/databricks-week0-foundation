# Day 3 – SQL Window Functions & Conditional Logic

## Objective
The objective of this session is to understand advanced SQL concepts such as Window Functions and Conditional Logic using CASE WHEN. These concepts are essential for performing analytical queries, ranking data, and deriving meaningful insights from datasets without modifying the original data structure.

---

## Topics Covered

### Window Functions Introduction
- Learned what Window Functions are and how they differ from aggregate functions
- Understood that window functions perform calculations across a set of rows related to the current row
- Unlike GROUP BY, they do not collapse rows

---

### OVER() Clause
- Learned the importance of the OVER() clause in window functions
- Understood that OVER() defines the window (set of rows) for the function
- Explored how calculations are applied across rows while keeping individual row details

---

### PARTITION BY
- Learned how to divide data into partitions (groups)
- Understood that calculations are performed separately within each partition
- Similar to GROUP BY but retains all rows
- Used for grouped analysis without losing row-level data

---

### ORDER BY in Window Functions
- Learned how ordering affects window function results
- Understood its role in ranking and cumulative calculations
- Explored how row order impacts function output

---

### Types of Window Functions

#### Ranking Functions
- ROW_NUMBER()
- RANK()
- DENSE_RANK()
- Understood differences between ranking methods
- Learned how ranking handles duplicate values

#### Aggregate Window Functions
- SUM()
- AVG()
- COUNT()
- Applied these functions using OVER() for running and grouped calculations

---

### CASE WHEN (Conditional Logic)
- Learned how to apply conditional logic in SQL queries
- Used CASE WHEN to create new derived columns
- Implemented multiple conditions for categorizing data
- Understood how to handle default cases using ELSE

---

## Practice Work Done

### Window Functions Practice
- Applied ROW_NUMBER(), RANK(), and DENSE_RANK() on datasets
- Practiced PARTITION BY for grouped analysis
- Used ORDER BY within window functions
- Explored cumulative and grouped calculations
- Compared results with normal aggregate functions

---

### CASE WHEN Practice
- Created conditional columns based on specific conditions
- Categorized data into different groups
- Applied multiple conditions in a single query
- Practiced real-time scenarios for data classification

---

## Key Differences Learned

### GROUP BY vs WINDOW FUNCTIONS
- GROUP BY reduces rows by aggregation
- Window functions retain all rows while adding calculated values

---

### RANK vs DENSE_RANK vs ROW_NUMBER
- ROW_NUMBER(): Assigns unique numbers to each row
- RANK(): Skips ranks when duplicates exist
- DENSE_RANK(): Does not skip ranks for duplicates

---

## How I Practiced Today
Today, I focused on understanding how window functions work internally by applying them to sample datasets. I experimented with PARTITION BY to group data and used ORDER BY to control ranking results. I practiced different ranking functions and compared their outputs to understand their differences. Additionally, I used CASE WHEN to apply conditional logic and categorize data based on different conditions. I repeated exercises multiple times to strengthen my understanding and improve accuracy.

---

## Challenges Faced
- Understanding the difference between GROUP BY and PARTITION BY
- Confusion between RANK and DENSE_RANK
- Writing correct syntax for CASE WHEN conditions
- Applying multiple conditions effectively

---

## How I Overcame Challenges
- Practiced multiple examples for each concept
- Compared outputs of different functions
- Broke down queries step-by-step
- Repeated exercises to gain clarity

---

## Key Takeaways
- Window functions are powerful for analytical queries
- PARTITION BY allows grouped calculations without losing data
- ORDER BY controls ranking and cumulative results
- CASE WHEN helps in applying conditional transformations
- Understanding differences between ranking functions is important

---

## Outcome
- Gained strong understanding of window functions
- Learned how to use PARTITION BY and OVER() effectively
- Understood ranking and analytical functions
- Improved skills in writing conditional SQL queries using CASE WHEN
- Built confidence in handling complex SQL queries

---
