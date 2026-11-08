# E-Commerce Business Intelligence & Customer Analytics

## Project Overview

The **E-Commerce Business Intelligence & Customer Analytics** project focuses on analyzing e-commerce business data to understand sales performance, customer behavior, product performance, payment patterns, and order delivery operations.

The project uses the Olist Brazilian E-Commerce Public Dataset and combines Python, PostgreSQL, SQL, and Power BI to transform raw data into meaningful business insights through interactive dashboards.

## Problem Statement

E-commerce businesses generate large amounts of data related to customers, orders, products, payments, and deliveries. Analyzing this data manually makes it difficult to identify business trends and operational issues.

This project aims to organize, process, and analyze e-commerce data to support data-driven business decisions.

## Project Objectives

- Analyze overall sales and revenue performance.
- Understand customer distribution and purchasing behavior.
- Identify top-performing product categories and sellers.
- Analyze payment methods and installment patterns.
- Evaluate order status and delivery performance.
- Build interactive Power BI dashboards for business insights.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data reading, profiling, and cleaning |
| Pandas | Data manipulation and processing |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| PostgreSQL | Relational database management |
| SQL | Business data analysis |
| Power BI | Interactive dashboard development |
| Power Query | Data transformation |
| DAX | Measures and KPI calculations |
| Visual Studio Code | Development environment |

## Dataset Overview

The project uses the Olist Brazilian E-Commerce Public Dataset.

The dataset contains nine tables:

1. Customers
2. Orders
3. Order Items
4. Payments
5. Products
6. Sellers
7. Reviews
8. Geolocation
9. Product Category Translation

The dataset includes information about customer locations, orders, products, payments, sellers, reviews, and delivery operations.

## Project Workflow

### 1. Data Reading

- Imported the nine CSV datasets using Python and Pandas.
- Examined dataset dimensions and column information.
- Checked missing values and basic data structure.

### 2. Data Profiling

- Checked duplicate records.
- Analyzed missing values.
- Examined order status distribution.
- Reviewed payment methods and product categories.
- Studied price and freight statistics.

### 3. Data Cleaning and Preparation

- Handled missing product category values.
- Filled missing review titles and messages.
- Examined missing delivery dates based on order status.
- Exported processed datasets into the processed data folder.

### 4. Database Management

- Used PostgreSQL to store and manage the nine dataset tables.
- Organized the data under the `ecommerce` schema.
- Established relationships between relevant tables.

### 5. SQL Analysis

Created four SQL scripts covering:

- Revenue Analysis
- Customer Analysis
- Product Analysis
- Order & Delivery Analysis

### 6. Power BI Dashboard Development

Developed four interactive dashboard pages using Power BI:

- Overview Dashboard
- Customer Analytics
- Payment Analytics
- Order & Delivery Analytics

## Dashboard Overview

### 1. Overview Dashboard

Provides a high-level view of business performance through revenue, delivered orders, average order value, customer metrics, product categories, monthly revenue trends, payment distribution, and geographical analysis.

### 2. Customer Analytics

Analyzes customer distribution across states and cities, customer metrics, and geographical purchasing patterns.

### 3. Payment Analytics

Examines payment revenue, payment method distribution, and installment patterns to understand customer payment preferences.

### 4. Order & Delivery Analytics

Analyzes order status distribution, average delivery time, monthly delivery performance, and delayed deliveries.

## Key Performance Indicators

The dashboards include important business KPIs such as:

- Total Delivered Revenue
- Total Delivered Orders
- Average Revenue per Delivered Order
- Total Unique Customers
- Total Payment Revenue
- Average Delivery Time

**Metric definitions:**
- Total Delivered Revenue is calculated using the item price of delivered orders and excludes freight charges.
- Average Revenue per Delivered Order is calculated by dividing delivered revenue by delivered orders.
- Total Unique Customers counts distinct customer identities.

## Project Folder Structure

```text
Ecommerce_Business_Intelligence_Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── documentation/
│   ├── 01_Project_Overview.docx
│   ├── 02_Technology_Stack.docx
│   ├── 03_Data_Processing_and_Methodology.docx
│   └── 04_Business_Insights_and_Recommendations.docx
│
├── powerbi/
│   └── Ecommerce_Business_Intelligence_Analytics.pbix
│
├── reports/
│   ├── dashboard_screenshots/
│   │   ├── Screenshot_1.png
│   │   ├── Screenshot_2.png
│   │   ├── Screenshot_3.png
│   │   └── Screenshot_4.png
│   │
│   └── Ecommerce_Business_Intelligence_Analytics.pdf
│
├── scripts/
│   ├── 01_data_reading.py
│   ├── 02_data_profiling.py
│   ├── 03_data_cleaning.py
│   └── 04_python_eda.py
│
├── sql/
│   ├── 01_revenue_analysis.sql
│   ├── 02_customer_analysis.sql
│   ├── 03_product_analysis.sql
│   └── 04_order_delivery_analysis.sql
│
├── .gitignore
└── README.md
```

## Business Value

This project demonstrates how raw e-commerce data can be transformed into structured information and actionable business insights.

It helps identify revenue patterns, understand customer distribution, evaluate payment preferences, recognize product performance, and monitor delivery operations.

## Conclusion

The project combines Python-based data preparation, PostgreSQL database management, SQL analysis, and Power BI visualization into an end-to-end Business Intelligence workflow.

It demonstrates practical applications of data analytics and business intelligence techniques in the e-commerce domain.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Project Category: Business Intelligence & Data Analytics
Dataset: Olist Brazilian E-Commerce Public Dataset
Tools: Python, PostgreSQL, SQL, Power BI