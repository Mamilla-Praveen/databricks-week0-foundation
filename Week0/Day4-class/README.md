# Phase – SQL Data Cleaning & Transformation

## Objective
In this phase, the goal is to understand how to use SQL functions to clean and transform data. The focus is on handling missing values, formatting text data, and working with date-related information.

---

## Problem Summary
The datasets used in this phase contained:

- Missing (NULL) values that could affect calculations  
- Text data in inconsistent formats (uppercase, lowercase, extra spaces)  
- Date columns that required extraction and comparison  

The tasks performed were:

- Handle NULL values properly  
- Standardize and clean text data  
- Extract meaningful insights from date columns  
- Apply classification logic based on conditions  

---

## Approach
- Identified columns with missing or inconsistent data  
- Applied appropriate NULL-handling techniques to avoid errors  
- Cleaned and formatted string data for consistency  
- Used date-based operations to calculate differences and extract components  
- Applied conditional logic to categorize data  

---

## Key Transformations Used

### NULL Functions
These functions are used to handle missing values in the dataset.

- Replaced NULL values with default values to prevent calculation errors  
- Ensured mathematical operations do not return NULL results  
- Compared values safely without unexpected outputs  

**Importance:**  
Handling NULL values is critical because ignoring them can lead to incorrect results in aggregations and calculations.

---

### String Functions
These functions are used to clean and standardize text data.

- Converted text to uppercase or lowercase for consistency  
- Formatted names into proper readable format  
- Extracted specific parts of a string when needed  
- Removed unnecessary spaces or unwanted characters  

**Importance:**  
String functions improve data quality and make the output more readable and consistent, which is important for reporting and analysis.

---

### Date Functions
These functions help in working with date and time data.

- Extracted components such as year or month from a date  
- Calculated the difference between two dates  
- Identified current date for comparison  
- Converted date values into meaningful formats  

**Importance:**  
Date functions are essential for time-based analysis such as calculating experience, delivery time, or duration.

---

## Output / Results
The transformations resulted in:

- Clean datasets with properly handled NULL values  
- Consistent and well-formatted text data  
- Accurate date-based calculations and insights  
- Categorized outputs based on business rules  

---

## Data Engineering Considerations
- Proper handling of NULL values ensures data reliability  
- Consistent string formatting improves data usability  
- Accurate date calculations are crucial for time-based decisions  
- Applying logic-based classification helps in business understanding  

---

## Challenges Faced
- Managing NULL values in calculations without affecting results  
- Choosing the correct function for string manipulation  
- Understanding how date differences are calculated  
- Applying correct conditions for classification  

---

## Learnings
- Importance of cleaning data before performing analysis  
- Practical use of NULL functions in real-world datasets  
- How string functions enhance data presentation  
- Role of date functions in deriving meaningful insights  
- Use of conditional logic for categorizing data  

---
