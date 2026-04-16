# 📘 Day 9 - Delta Lake: MERGE, Time Travel & Log Files

## 📌 Overview

Day 9 focuses on advanced Delta Lake operations that are widely used in real-world data engineering projects. This includes handling incremental data using MERGE, exploring historical data using Time Travel, and understanding Delta Lake log files.

---

## 🔹 MERGE (UPSERT Operation)

### 📖 What is MERGE?

MERGE is used to perform **INSERT, UPDATE, and DELETE** operations in a single command.

### 🚀 Why MERGE is Important?

* Handles **incremental data (CDC)**
* Avoids full data reload
* Ensures **ACID transactions**
* Used in real-time pipelines

### ⚙️ Key Concepts

* **WHEN MATCHED** → UPDATE or DELETE existing records
* **WHEN NOT MATCHED** → INSERT new records

---

## 🔹 Time Travel

### 📖 What is Time Travel?

Time Travel allows you to **access previous versions of data** stored in Delta tables.

### 🚀 Why it is Useful?

* Recover deleted data
* Debug data issues
* Audit changes over time

### ⚙️ Key Features

* Query older versions using **version number**
* Query data using **timestamp**
* Restore table to a previous state

---

## 🔹 DESCRIBE HISTORY

### 📖 What is it?

Shows the **history of operations** performed on a Delta table.

### 📊 Information Includes:

* Version number
* Operation type (WRITE, UPDATE, DELETE, MERGE)
* Timestamp
* User details

### 🚀 Use Cases:

* Data auditing
* Tracking pipeline changes
* Debugging

---

## 🔹 Delta Log Files (_delta_log)

### 📖 What are Delta Log Files?

Delta Lake stores all transaction details inside the `_delta_log` folder.

### 📂 Contents:

* JSON files → Transaction logs
* Parquet files → Checkpoints

### 🚀 Why Important?

* Enables **ACID transactions**
* Supports **Time Travel**
* Maintains **data consistency**

---

## 🔥 Real-World Flow

1. Data is ingested (batch/stream)
2. Changes are captured (CDC)
3. MERGE is used to apply updates
4. Delta logs track every change
5. Time Travel allows rollback if needed

---

## 💡 Key Takeaways

* MERGE is used for **incremental processing**
* Time Travel helps in **data recovery**
* Log files ensure **data reliability**
* Delta Lake provides **scalable and fault-tolerant storage**

---

## 🎯 Conclusion

Day 9 covers critical Delta Lake concepts that are essential for building **robust, real-time data pipelines**. Understanding MERGE, Time Travel, and Log Files is key for any Data Engineer working with modern data platforms like Databricks.

---

