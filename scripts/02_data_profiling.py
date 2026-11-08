import pandas as pd


# 1. ORDERS DATASET
orders = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\raw\1_olist_orders_dataset.csv"
)

# 2. CUSTOMERS DATASET
customers = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/2_olist_customers_dataset.csv"
)

# 3. ORDER ITEMS DATASET

order_items = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\raw\3_olist_order_items_dataset.csv"
)

# 4. PAYMENTS DATASET

payments = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\raw\4_olist_order_payments_dataset.csv"
)

# 5. REVIEWS DATASET

reviews = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/5_olist_order_reviews_dataset.csv"
)

# 6. PRODUCT DATASET

products = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/6_olist_products_dataset.csv"
)

# 7. SELLLERS DATASET

sellers = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/7_olist_sellers_dataset.csv"
)

# 8. GEOLOCATION DATASET

geolocation = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/8_olist_geolocation_dataset.csv"
)

# 9. CATEGORY_TRANSLATION 

category_translation = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/9_product_category_name_translation.csv"
)

# DUPLICATE RECORDS CHECK

print("\nDUPLICATE RECORDS")

print("Orders:", orders.duplicated().sum())
print("Customers:", customers.duplicated().sum())
print("Order Items:", order_items.duplicated().sum())
print("Payments:", payments.duplicated().sum())
print("Reviews:", reviews.duplicated().sum())
print("Products:", products.duplicated().sum())
print("Sellers:", sellers.duplicated().sum())
print("Geolocation:", geolocation.duplicated().sum())
print("Category Translation:", category_translation.duplicated().sum())


# Geolocation Duplication

print(geolocation[geolocation.duplicated()].head())
print(geolocation.shape)


# Geolocation Duplicate Values and percentage of Duplicate from total

total_records = geolocation.shape[0]
duplicate_records = geolocation.duplicated().sum()
duplicate_percentage = (duplicate_records / total_records) * 100
print("Total Records:", total_records)
print("Duplicate Records:", duplicate_records)
print("Duplicate Percentage:", round(duplicate_percentage, 2), "%")


# Check Missinf Values

print("Payments Missing Values:")
print(payments.isna().sum())

print("Reviews Missing Values:")
print(reviews.isna().sum())

print("Products Missing Values:")
print(products.isna().sum())

print("Sellers Missing Values:")
print(sellers.isna().sum())

print("Geolocation Missing Values:")
print(geolocation.isna().sum())

print("Category Translation Missing Values:")
print(category_translation.isna().sum())


# Check review scores 1-star to 5-star

print(reviews["review_score"].value_counts().sort_index())


# Check Product Category

print(products["product_category_name"].value_counts().head(10))


# Translate category names

print(category_translation.head(10))


# Check product prices

print(order_items[["price", "freight_value"]].describe())


# Check order-item records

print(order_items.head())


# Check order status distribution

print(orders["order_status"].value_counts())


# Check payment methods

print(payments["payment_type"].value_counts())




