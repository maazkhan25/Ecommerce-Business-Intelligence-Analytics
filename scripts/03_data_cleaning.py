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


# PRODUCT DATA CLEANING

# Identify the affected product records
print(products[products.isna().any(axis=1)].head(10))

print(products[products.isna().any(axis=1)].isna().sum())


# Check whether the two groups overlap
print(products[products["product_weight_g"].isna()])


# Handle the 610 records
print(products[products["product_category_name"].isna()]["product_id"].isna().sum())


# Apply a safe cleaning operation
products["product_category_name"] = products["product_category_name"].fillna("unknown")

print(products["product_category_name"].isna().sum())


# Verify the product dataset
print(products["product_category_name"].value_counts().head(5))

print(products["product_category_name"].value_counts().tail())

print(products["product_category_name"].value_counts()["unknown"])


# Save the cleaned CSV in processed Folder 
products.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_products.csv", index=False)



# REVIEWS DATA CLEANING

# NULL values Replace
reviews["review_comment_title"] = reviews["review_comment_title"].fillna("No title")

reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No comment")

# Verify it
print(reviews[["review_comment_title", "review_comment_message"]].isna().sum())

# Save the cleaned Reviews datase
reviews.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_reviews.csv", index=False)



# ORDERS DATA CLEANING

# Check the NULL Values
print(orders.isna().sum())

# Check missing delivery dates by order status
print(pd.crosstab(orders["order_status"], orders["order_delivered_customer_date"].isna()))

# We are Keeping all missing dates as NaN. Do not invent dates or delete these orders.
# Save the cleaned Orders dataset
orders.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_orders.csv", index=False)



# NO MORE DATA CLEANING AVAILABLE SO DIRECTLY SAVE THEIR FILES

# handle the order_items dataset. It had zero missing values and zero exact duplicate records.
# No cleaning is required for it right now.

# Save the cleaned Orders_Items dataset
order_items.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_order_items.csv", index=False)

# Save the Payments dataset
payments.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_payments.csv", index=False)

# Save the Sellers dataset
sellers.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_sellers.csv", index=False)

# Remove exact duplicate geolocation records
duplicate_count = geolocation.duplicated().sum()

geolocation = geolocation.drop_duplicates().copy()

print("Duplicates Removed:", duplicate_count)
print("Final Geolocation Shape:", geolocation.shape)

# Save the Geolocation dataset
geolocation.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_geolocation.csv", index=False)

# Save Category Translation
category_translation.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_category_translation.csv", index=False)

# Save Customers dataset
customers.to_csv(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_customers.csv", index=False)



# VERIFYING ALL THE PROCESSED FILE
import os

print(os.listdir(r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed"))


