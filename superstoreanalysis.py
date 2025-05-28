# superstore_sales_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\user\Downloads\archive (1)\Sample - Superstore.csv", encoding='ISO-8859-1')

# Basic dataset info
print("Dataset Info:")
print(df.info())
print("\nMissing values:")
print(df.isnull().sum())

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Month-Year'] = df['Order Date'].dt.to_period('M')

# ---------- EDA & Visualizations ---------- #

# Sales by Category
plt.figure(figsize=(8, 4))
df.groupby('Category')['Sales'].sum().sort_values().plot(kind='bar', color='skyblue')
plt.title("Total Sales by Category")
plt.ylabel("Sales ($)")
plt.xlabel("Category")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# Sales over Time
plt.figure(figsize=(12, 6))
df.groupby('Month-Year')['Sales'].sum().plot()
plt.title("Monthly Sales Trend")
plt.ylabel("Sales ($)")
plt.xlabel("Month-Year")
plt.grid()
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# Top 10 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_products.plot(kind='barh', color='green')
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales ($)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# Profit by Region
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
plt.figure(figsize=(8, 4))
region_profit.plot(kind='bar', color='orange')
plt.title("Profit by Region")
plt.ylabel("Profit ($)")
plt.xlabel("Region")
plt.tight_layout()
plt.savefig("region_profit.png")
plt.show()

# ---------- Summary Metrics ---------- #

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
avg_profit = df['Profit'].mean()

print("\n========== Summary ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit per Order: ${avg_profit:,.2f}")

# Optional: Save cleaned dataset
df.to_csv("cleaned_superstore.csv", index=False)
