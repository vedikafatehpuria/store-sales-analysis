# store_sales_analysis.py

# 1. Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 2. Load the dataset
data = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

# 3. Basic Info
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

# 4. Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# 5. Total Sales and Profit
total_sales = data['Sales'].sum()
total_profit = data['Profit'].sum()
print(f"\nTotal Sales: {total_sales}")
print(f"Total Profit: {total_profit}")

# 6. Profit by Category
category_profit = data.groupby('Category')['Profit'].sum()
plt.figure(figsize=(8,6))
category_profit.plot(kind='bar', color='skyblue')
plt.title('Profit by Category')
plt.ylabel('Total Profit')
plt.xlabel('Category')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('profit_by_category.png')
plt.close()

# 7. Sales vs Profit Scatter Plot
plt.figure(figsize=(8,6))
sns.scatterplot(x='Sales', y='Profit', hue='Category', data=data)
plt.title('Sales vs Profit by Category')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.tight_layout()
plt.savefig('sales_vs_profit.png')
plt.close()

# 8. Sales and Profit by Region
region_sales_profit = data.groupby('Region')[['Sales', 'Profit']].sum()
region_sales_profit.plot(kind='bar', figsize=(8,6))
plt.title('Sales and Profit by Region')
plt.ylabel('Amount ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_profit_by_region.png')
plt.close()

# 9. Top 10 Products by Profit
top_products = data.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,6))
top_products.plot(kind='barh', color='green')
plt.title('Top 10 Products by Profit')
plt.xlabel('Total Profit')
plt.tight_layout()
plt.savefig('top_products_by_profit.png')
plt.close()

print("\nAnalysis completed! Charts have been saved as PNG images.")
