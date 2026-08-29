import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("retail_sales_dataset.csv", sep="\t", engine="python")
print("Dataset Loaded Successfully!\n")

# First 5 records
print("First 5 Records:")
print(df.head())

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

print("\nDate converted successfully!")
print(df['Date'].dtype)

print("\n===== SALES KPIs =====")

total_sales = df['Total Amount'].sum()
total_quantity = df['Quantity'].sum()
total_transactions = df['Transaction ID'].nunique()
average_sales = df['Total Amount'].mean()

print("Total Sales:", total_sales)
print("Total Quantity Sold:", total_quantity)
print("Total Transactions:", total_transactions)
print("Average Transaction Value:", round(average_sales, 2))

category_sales = df.groupby('Product Category')['Total Amount'].sum().sort_values(ascending=False)

print("\n===== SALES BY CATEGORY =====")
print(category_sales) 


plt.figure(figsize=(8, 5))

category_sales.plot(kind='bar')

plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

gender_sales = df.groupby('Gender')['Total Amount'].sum()

print("\n===== SALES BY GENDER =====")
print(gender_sales)

plt.figure(figsize=(7, 5))

gender_sales.plot(kind='bar')

plt.title('Total Sales by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# ==========================================
# MONTHLY SALES ANALYSIS
# ==========================================

# Create Month column
df['Month'] = df['Date'].dt.month_name()

# Arrange months in correct order
month_order = [
    'January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August',
    'September', 'October', 'November', 'December'
]

df['Month'] = pd.Categorical(
    df['Month'],
    categories=month_order,
    ordered=True
)

# Calculate monthly sales
monthly_sales = df.groupby(
    'Month',
    observed=False
)['Total Amount'].sum()

print("\n===== MONTHLY SALES =====")
print(monthly_sales)

plt.figure(figsize=(12, 6))

monthly_sales.plot(kind='line', marker='o')

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# ==========================================
# AGE GROUP ANALYSIS
# ==========================================

# Create age groups
bins = [17, 25, 35, 45, 55, 65]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65']

df['Age Group'] = pd.cut(
    df['Age'],
    bins=bins,
    labels=labels
)

# Sales by age group
age_group_sales = df.groupby(
    'Age Group',
    observed=False
)['Total Amount'].sum()

print("\n===== SALES BY AGE GROUP =====")
print(age_group_sales)

plt.figure(figsize=(9, 5))

age_group_sales.plot(kind='bar')

plt.title('Total Sales by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Sales')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

age_group_customers = df.groupby(
    'Age Group',
    observed=False
)['Customer ID'].nunique()

print("\n===== CUSTOMERS BY AGE GROUP =====")
print(age_group_customers)

plt.figure(figsize=(9, 5))

age_group_customers.plot(kind='bar')

plt.title('Number of Customers by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Number of Customers')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()