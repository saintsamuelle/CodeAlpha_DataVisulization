import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visualization folder
os.makedirs("visualizations", exist_ok=True)

# Load data
df = pd.read_csv("data/sales_data.csv")

# Create revenue column
df['revenue'] = df['units_sold'] * df['unit_price']

# 1. Monthly Sales Trend
monthly_sales = df.groupby('month')['revenue'].sum()

plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("visualizations/monthly_sales_trend.png")
plt.close()

# 2. Sales by Region
region_sales = df.groupby('region')['revenue'].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.savefig("visualizations/sales_by_region.png")
plt.close()

# 3. Product Sales Comparison
product_sales = df.groupby('product')['revenue'].sum()

plt.figure()
product_sales.plot(kind='bar')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.savefig("visualizations/product_sales.png")
plt.close()

# 4. Revenue Distribution
plt.figure()
plt.hist(df['revenue'])
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.savefig("visualizations/revenue_distribution.png")
plt.close()

# 5. Correlation Heatmap
plt.figure()
sns.heatmap(df[['units_sold', 'unit_price', 'revenue']].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.savefig("visualizations/correlation_heatmap.png")
plt.close()

print("Sales visualizations generated successfully!")
