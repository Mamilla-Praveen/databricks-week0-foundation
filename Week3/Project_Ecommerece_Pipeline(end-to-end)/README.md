## 📊 E-Commerce Data Pipeline using Medallion Architecture (Databricks)

## 🚀 Business Pitch
In today’s data-driven world, e-commerce companies such as Amazon and Flipkart generate massive volumes of data from customer purchases, product interactions, and transactions.

However, raw data alone cannot help businesses make decisions.

Businesses need answers like:
- Which products generate the highest revenue?
- What are the current sales trends?
- Who are the most valuable customers?

The main challenge is:
👉 Raw data is incomplete, inconsistent, and not ready for analysis  

---

## 💡 Solution
To solve this problem, we built an end-to-end data pipeline using Medallion Architecture in Databricks.

This pipeline transforms raw data into clean, structured, and business-ready insights, enabling:
- Better decision-making  
- Scalable data processing  
- Advanced analytics and ML  

---

## 🏗️ Architecture Overview
Raw Data → Bronze → Silver → Gold → Dashboards → Insights → ML

Explanation:
- Bronze Layer → Raw data storage  
- Silver Layer → Data cleaning and transformation  
- Gold Layer → Business insights and aggregations  
- Dashboard Layer → Visualization  

---

## 📂 Project Structure
E-Commerce Sales Pipeline/
│
├── bronze/        # Raw data ingestion
├── silver/        # Data cleaning & transformation
├── gold/          # Business logic & aggregations
├── dashboards/    # Visualization layer
├── datasets/      # Input data
├── notebooks/     # Databricks notebooks
└── README.md

---

## 📁 Dataset Description
The dataset represents real-world e-commerce operations including customers, orders, products, and transactions.

---

## 👤 Customers Table
Columns:
- customer_id → Unique customer identifier  
- customer_unique_id → Identifies a unique user across orders  
- customer_zip_code_prefix → Customer location  
- customer_city → Customer city  
- customer_state → Customer state  

Purpose:
Used for customer segmentation and location-based analysis.

---

## 📦 Orders Table
Columns:
- order_id → Unique order identifier  
- customer_id → Links to customer  
- order_status → Order status  
- order_purchase_timestamp → Purchase time  
- order_approved_at → Approval time  
- order_delivered_carrier_date → Shipped date  
- order_delivered_customer_date → Delivered date  
- order_estimated_delivery_date → Expected delivery  

Purpose:
Used to track order lifecycle and delivery performance.

---

## 🛍️ Order Items Table
Columns:
- order_id → Links to order  
- order_item_id → Item identifier  
- product_id → Product reference  
- seller_id → Seller identifier  
- shipping_limit_date → Shipping deadline  
- price → Product price  
- freight_value → Shipping cost  

Purpose:
Used to calculate revenue and analyze product-level sales.

---

## 📦 Products Table
Columns:
- product_id → Unique product ID  
- product_category_name → Product category  
- product_name_lenght → Name length  
- product_description_lenght → Description length  
- product_photos_qty → Number of images  
- product_weight_g → Weight  
- product_length_cm → Length  
- product_height_cm → Height  
- product_width_cm → Width  

Purpose:
Used for product analysis and category insights.

---

## 🔗 Data Relationships
- customer_id → Customers ↔ Orders  
- order_id → Orders ↔ Order Items  
- product_id → Order Items ↔ Products  

👉 Enables full transaction-level analysis  

---

## 🥉 Bronze Layer (Raw Data Layer)
Purpose:
Stores raw data as it is without any modifications.

Key Activities:
- Data ingestion from CSV files  
- Stored as Delta tables in Databricks  
- No transformations applied  

Outcome:
- Maintains original data  
- Ensures traceability  
- Supports reprocessing  

---

## 🥈 Silver Layer (Data Cleaning & Transformation)
Purpose:
Transforms raw data into clean, structured, and reliable data.

Key Operations:
- Handling missing values  
- Data type conversions  
- Data standardization  
- Joining multiple tables  

Output:
A unified dataset with:
- Customer details  
- Product details  
- Order information  
- Transaction values  

Business Impact:
- Improves data accuracy  
- Eliminates inconsistencies  
- Enables reliable analytics  

---

## 🥇 Gold Layer (Business Insights Layer)
Purpose:
Prepares data for reporting, dashboards, and business insights.

⭐ Sales Fact Table
Description:
A centralized table representing business transactions.

Columns:
    --> "order_id",
    --> "order_item_id",
    --> "customer_id",
    --> "customer_city",
    --> "customer_state",
    --> "product_id",
    --> "product_category_name",
    --> "price",
    --> "freight_value",
    --> "order_status",
    --> "order_purchase_timestamp",
    --> "order_delivered_customer_date"

Importance:
- Core table for analytics  
- Supports KPI calculations  

---

## 📈 KPIs Implemented
We calculated the following key metrics:
- Total Revenue  
- Top Selling Products  
- Revenue by Category  
- Customer Purchase Analysis  
- Sales Trends Over Time  
- Average Order Value (AOV)  

👉 These KPIs help measure performance and guide business decisions.  

---

## 📊 Dashboards (Business Visualization Layer)
Purpose:
We built dashboards that help businesses understand data visually.

Features:
- Revenue trends  
- Product performance  
- Category analysis  
- Customer insights  

Business Value:
- Monitor business performance  
- Identify trends and patterns  
- Make faster data-driven decisions  

👉 Dashboards are the final layer where business users interact with data  

---

## 🤖 Machine Learning Extension
Using Silver and Gold data, we can implement:
- Recommendation systems  
- Customer segmentation  
- Purchase prediction  

Example:
👉 Suggest products based on customer behavior and search patterns  

---

## 🛠️ Tools & Technologies
- Databricks  
- PySpark  
- SQL  
- Delta Lake  

---

## 📈 Key Outcomes
- Built a scalable data pipeline  
- Cleaned and transformed raw data  
- Created Sales Fact Table  
- Generated KPIs  
- Developed dashboards for business insights  

---

## 🎯 Conclusion
This project demonstrates how:
- Raw data can be transformed into meaningful insights  
- Structured pipelines improve data quality  
- Businesses can make better decisions using data  

👉 It bridges the gap between data engineering and business intelligence  

---

## ✨ Future Enhancements
- Real-time data streaming  
- Advanced ML models  
- Integration with Power BI / Tableau  
- Automated KPI monitoring  
