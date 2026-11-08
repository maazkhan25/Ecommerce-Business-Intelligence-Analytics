import pandas as pd


# 1. ORDERS DATASET
orders = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\raw\1_olist_orders_dataset.csv"
)
print(orders.head())
print (orders.shape)
print (orders.columns)
orders.info()
print (orders.isna().sum())


# 2. CUSTOMERS DATASET
customers = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/2_olist_customers_dataset.csv"
)

print(customers.head())
print (customers.shape)
print (customers.columns)
customers.info()
print (customers.isna().sum())


# 3. ORDER ITEMS DATASET

order_items = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\raw\3_olist_order_items_dataset.csv"
)

print(order_items.head())
print (order_items.shape)
print (order_items.columns)
order_items.info()
print (order_items.isna().sum())


# 4. PAYMENTS DATASET

payments = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\raw\4_olist_order_payments_dataset.csv"
)

print(payments.head())
print (payments.shape)
print (payments.columns)
payments.info()
print (payments.isna().sum())


# 5. REVIEWS DATASET

reviews = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/5_olist_order_reviews_dataset.csv"
)

print (reviews.head())
print (reviews.shape)
print (reviews.columns)
reviews.info()
print (reviews.isna().sum())


# 6. PRODUCT DATASET

products = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/6_olist_products_dataset.csv"
)

print (products.head())
print (products.shape)
print (products.columns)
products.info()
print (products.isna().sum())


# 7. SELLLERS DATASET

sellers = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/7_olist_sellers_dataset.csv"
)

print (sellers.head())
print (sellers.shape)
print (sellers.columns)
sellers.info()
print (sellers.isna().sum())


# 8. GEOLOCATION DATASET

geolocation = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/8_olist_geolocation_dataset.csv"
)

print (geolocation.head()) 
print (geolocation.shape)
print (geolocation.columns)
geolocation.info()
print (geolocation.isna().sum())

# 9. CATEGORY_TRANSLATION 

category_translation = pd.read_csv(
    r"C:/Users/Lenovo/Desktop/Ecommerce_Business_Intelligence_Analytics/data/raw/9_product_category_name_translation.csv"
)

print (category_translation.head())
print (category_translation.shape)
print (category_translation.columns)
category_translation.info()
print (category_translation.isna().sum())

















