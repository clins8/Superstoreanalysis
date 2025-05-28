# Importing the libraries I need for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Load the Superstore dataset
df = pd.read_csv(r"C:\Users\user\Downloads\archive (1)\Sample - Superstore.csv", encoding='ISO-8859-1')

#Quick look at the dataset structure and missing values
print("Basic Dataset Info:\n")
print(df.info())

print("\nMissing Values Check:")
print(df.isnull().sum())

# Convert the date columns to datetime format for time-based analysis
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create a new column for Month-Year to observe trends over time
df['Month-Year'] = df['Order Date'].dt.to_period('M')


# Exploratory Data Analysis (EDA) & Visualizations

#Total Sales by Category
plt.figure(figsize=(8, 4))
category_sales = df.groupby('Category')['Sales'].sum().sort_values()
category_sales.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Category")
plt.ylabel("Sales in USD")
plt.xlabel("Product Category")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

#Monthly Sales Trend Over Time
plt.figure(figsize=(12, 6))
monthly_sales = df.groupby('Month-Year')['Sales'].sum()
monthly_sales.plot(marker='o')
plt.title("Monthly Sales Trend")
plt.ylabel("Sales in USD")
plt.xlabel("Month-Year")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

#Top 10 Best-Selling Products
plt.figure(figsize=(10, 6))
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='barh', color='green')
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales in USD")
plt.gca().invert_yaxis()  # To show the highest at the top
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# Profit by Region
plt.figure(figsize=(8, 4))
region_profit = df.groupby('Region')['Profit'].sum().sort_values()
region_profit.plot(kind='bar', color='orange')
plt.title("Profit by Region")
plt.ylabel("Profit in USD")
plt.xlabel("Region")
plt.tight_layout()
plt.savefig("region_profit.png")
plt.show()


# Calculating total and average metrics - summary statistics 
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
average_profit = df['Profit'].mean()

# Print the summary insights
print("\n========== Summary Metrics ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Average Profit per Order: ${average_profit:,.2f}")

