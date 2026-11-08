
import pandas as pd


# 1. ORDERS DATASET
orders = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_orders.csv"
)

# 2. ORDER ITEMS DATASET
order_items = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_order_items.csv"
)

# 3. CUSTOMERS DATASET
customers = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_customers.csv"
)

# 4. PRODUCTS DATASET
products = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_products.csv"
)

# 5. PAYMENTS DATASET
payments = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_payments.csv"
)

# 6. REVIEWS DATASET
reviews = pd.read_csv(
    r"C:\Users\Lenovo\Desktop\Ecommerce_Business_Intelligence_Analytics\data\processed\cleaned_reviews.csv"
)


# BASIC DATASET INFORMATION

print("ORDERS DATASET")
print(orders.shape)
print(orders.head())

print("\nORDER ITEMS DATASET")
print(order_items.shape)
print(order_items.head())

print("\nCUSTOMERS DATASET")
print(customers.shape)
print(customers.head())

print("\nPRODUCTS DATASET")
print(products.shape)
print(products.head())

print("\nPAYMENTS DATASET")
print(payments.shape)
print(payments.head())

print("\nREVIEWS DATASET")
print(reviews.shape)
print(reviews.head())





# 7. ORDER STATUS ANALYSIS

print("\nORDER STATUS DISTRIBUTION")
print(orders["order_status"].value_counts())


# 8. PRODUCT PRICE ANALYSIS

print("\nPRODUCT PRICE ANALYSIS")
print(order_items[["price", "freight_value"]].describe())


# 9. CUSTOMER REVIEW ANALYSIS

print("\nCUSTOMER REVIEW DISTRIBUTION")
print(reviews["review_score"].value_counts().sort_index())


# 10. PAYMENT METHOD ANALYSIS

print("\nPAYMENT METHOD DISTRIBUTION")
print(payments["payment_type"].value_counts())


# 11. PRODUCT CATEGORY ANALYSIS

print("\nTOP 10 PRODUCT CATEGORIES")
print(products["product_category_name"].value_counts().head(10))







# 12. TOTAL REVENUE ANALYSIS

delivered_orders = orders[
    orders["order_status"] == "delivered"
]

# Merge Orders and Order Items
sales = pd.merge(
    delivered_orders,
    order_items,
    on="order_id"
)

# Total Revenue
total_revenue = sales["price"].sum()

print("\nTOTAL REVENUE:", round(total_revenue, 2))


# 13. MONTHLY REVENUE ANALYSIS

sales["order_purchase_timestamp"] = pd.to_datetime(
    sales["order_purchase_timestamp"]
)

sales["month"] = sales["order_purchase_timestamp"].dt.month

monthly_revenue = sales.groupby("month")["price"].sum()

print("\nMONTHLY REVENUE")
print(monthly_revenue)





# 14. MONTHLY REVENUE VISUALIZATION

import matplotlib.pyplot as plt

plt.plot(monthly_revenue.index, monthly_revenue.values, '*b')

plt.title("Monthly Revenue Analysis")
plt.xlabel("Month")
plt.ylabel("Revenue (BRL)")

plt.show()





# 15. PRODUCT PRICE VS FREIGHT ANALYSIS

plt.scatter(
    order_items["price"],
    order_items["freight_value"]
)

plt.title("Product Price vs Freight Value")
plt.xlabel("Product Price")
plt.ylabel("Freight Value")

plt.show()




# 16. CUSTOMER REVIEW SCORE VISUALIZATION

review_count = reviews["review_score"].value_counts().sort_index()

plt.plot(review_count.index, review_count.values, '*b')

plt.title("Customer Review Score Distribution")
plt.xlabel("Review Score")
plt.ylabel("Number of Reviews")

plt.show()




# 17. PAYMENT METHOD VISUALIZATION

payment_count = payments["payment_type"].value_counts()

plt.plot(payment_count.index, payment_count.values, '*b')

plt.title("Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")

plt.show()




# 18. ORDER STATUS VISUALIZATION

order_status_count = orders["order_status"].value_counts()

plt.plot(order_status_count.index, order_status_count.values, '*b')

plt.title("Order Status Distribution")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.show()





# 19. TOP 10 PRODUCT CATEGORIES

category_count = products["product_category_name"].value_counts().head(10)

plt.plot(category_count.index, category_count.values, '*b')

plt.title("Top 10 Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Number of Products")

plt.show()





# 20. CUSTOMER SEGMENTATION DATA PREPARATION

# Merge customer information with sales data
sales = pd.merge(
    sales,
    customers[["customer_id", "customer_unique_id"]],
    on="customer_id"
)

# Calculate customer orders
customer_orders = sales.groupby("customer_unique_id")["order_id"].nunique()

# Calculate customer spending
customer_spending = sales.groupby("customer_unique_id")["price"].sum()

# Combine customer data
customer_data = pd.DataFrame({
    "total_orders": customer_orders,
    "total_spending": customer_spending
})

print("\nCUSTOMER SEGMENTATION DATA")
print(customer_data.head())

print("\nCUSTOMER DATA SHAPE")
print(customer_data.shape)





# 21. FEATURE SCALING

from sklearn.preprocessing import MinMaxScaler

X = customer_data[["total_orders", "total_spending"]]

mm = MinMaxScaler()

X_scaled = mm.fit_transform(X)

print("\nSCALED CUSTOMER DATA")
print(X_scaled[:5])






# 22. K-MEANS CLUSTERING

from sklearn.cluster import KMeans

model = KMeans(n_clusters=3, random_state=0, n_init='auto')

model.fit(X_scaled)

print("\nCUSTOMER CLUSTER LABELS")
print(model.labels_)

# Add cluster labels to customer data
customer_data["cluster"] = model.labels_

print("\nCUSTOMER DATA WITH CLUSTERS")
print(customer_data.head())




# 23. CUSTOMER CLUSTER VISUALIZATION

import numpy as np

x = np.array(X_scaled)

plt.scatter(
    x[:, 0],
    x[:, 1],
    c=model.labels_,
    cmap="autumn"
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Purchase Frequency (Scaled)")
plt.ylabel("Total Spending (Scaled)")

plt.show()




# 24. CUSTOMER SEGMENT ANALYSIS

cluster_analysis = customer_data.groupby("cluster").agg({
    "total_orders": "mean",
    "total_spending": "mean"
})

print("\nCUSTOMER SEGMENT ANALYSIS")
print(cluster_analysis)

print("\nCUSTOMER COUNT IN EACH CLUSTER")
print(customer_data["cluster"].value_counts())





# 25. CUSTOMER SEGMENT LABELS

customer_data["customer_segment"] = customer_data["cluster"].map({
    0: "Low Spending",
    1: "Frequent Buyers",
    2: "High Spending"
})

print("\nFINAL CUSTOMER SEGMENTS")
print(customer_data.head())

print("\nSEGMENT DISTRIBUTION")
print(customer_data["customer_segment"].value_counts())




# 26. EXPORT CUSTOMER SEGMENTS

customer_data.to_csv(
    "data/processed/customer_segments.csv"
)

print("\nCustomer Segmentation File Saved Successfully")
