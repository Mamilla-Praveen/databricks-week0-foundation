# Phase – PySpark Data Cleaning, Transformation & Regex

## Objective
In this phase, the goal is to perform data cleaning, transformation, and pattern extraction using PySpark and Regular Expressions (Regex). The focus is on handling real-world data issues such as inconsistent formats, missing values, and extracting meaningful patterns from text.

---

## Problem Summary
The datasets used in this phase contained:

- Text data with mixed patterns (alphabets + numbers)  
- Columns like email, phone, and IDs requiring pattern extraction  
- Missing (NULL) values in certain fields  
- Inconsistent formats in categorical columns  

The tasks performed were:

- Clean and standardize the data  
- Extract specific patterns using Regular Expressions  
- Handle NULL values effectively  
- Perform transformations using PySpark DataFrame operations  

---

## Approach
- Loaded the dataset into PySpark DataFrame  
- Inspected data for inconsistencies and missing values  
- Applied filtering conditions to extract required records  
- Used column transformations to clean and standardize data  
- Applied Regular Expressions to extract patterns from text fields  
- Performed sorting, deduplication, and data enrichment  
- Generated final structured output  

---

## Key Transformations Used

### Regular Expressions (Regex)
Regex was used to extract patterns from text-based columns such as:

- Extracting numbers from strings  
- Identifying patterns at the beginning or end of values  
- Extracting specific parts of emails (username, domain)  
- Extracting country codes from phone numbers  
- Separating alphabets and numeric values  

**Importance:**  
Regex helps in identifying and extracting meaningful patterns from unstructured text data, which is very common in real-world datasets.

---

### Data Filtering
- Applied conditions to filter rows based on specific column values  
- Used logical conditions to combine multiple filters  

**Importance:**  
Filtering helps in narrowing down the dataset to only relevant records for analysis.

---

### Column Transformations
- Renamed columns for better readability  
- Created new columns with constant or derived values  
- Standardized categorical values  

**Importance:**  
Transformations improve data consistency and prepare it for analysis.

---

### Conditional Logic
- Applied conditional rules to modify column values  
- Categorized data based on specific conditions  

**Importance:**  
Helps in applying business logic and making data more meaningful.

---

### NULL Handling
- Identified missing values in columns  
- Replaced NULL values with default values  

**Importance:**  
Prevents errors in processing and ensures accurate results.

---

### Sorting & Deduplication
- Sorted data based on one or more columns  
- Removed duplicate records  

**Importance:**  
Ensures clean and organized data for analysis.

---

### Date Functions
- Added current date columns  
- Calculated future and past dates  

**Importance:**  
Used for time-based tracking and analysis.

---

### String Operations
- Standardized text format (case conversion)  
- Split columns into structured formats  

**Importance:**  
Improves readability and usability of textual data.

---

## Output / Results
The following outputs were generated:

- Cleaned dataset with consistent formatting  
- Extracted patterns such as:
  - Email components  
  - Phone number country codes  
  - Numeric and alphabetic segments  
- Dataset with no NULL-related issues  
- Sorted and deduplicated data ready for analysis  

---

## Data Engineering Considerations
- Ensured proper handling of NULL values  
- Applied regex carefully to avoid incorrect pattern extraction  
- Maintained data consistency after transformations  
- Verified outputs after each transformation step  

---

## Challenges Faced
- Understanding complex regex patterns  
- Extracting specific parts of strings without errors  
- Handling mixed data types in columns  
- Managing NULL values during transformations  

---

## Learnings
- How Regular Expressions are used for pattern extraction  
- Importance of data cleaning in real-world scenarios  
- Practical usage of PySpark DataFrame transformations  
- Handling missing data effectively  
- Applying conditional logic for data standardization  

---

## Topics Covered
- Regular Expressions (pattern matching & extraction)  
- Data filtering and transformations  
- NULL value handling  
- String manipulation  
- Date operations  
- Sorting and deduplication  

---
