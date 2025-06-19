
import pandas as pd
import numpy as np

# -------- Homework 1 --------
print("Homework 1\n")

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# 1. Rename columns
df.rename(columns={'First Name': 'first_name', 'Age': 'age'}, inplace=True)

# 2. Print first 3 rows
print("First 3 rows:")
print(df.head(3))

# 3. Mean age
print("\nMean age:", df['age'].mean())

# 4. Select and print only 'first_name' and 'City'
print("\nName and City columns:")
print(df[['first_name', 'City']])

# 5. Add 'Salary' column with random values
df['Salary'] = np.random.randint(50000, 100000, size=len(df))
print("\nDataFrame with Salary column:")
print(df)

# 6. Summary statistics
print("\nSummary statistics:")
print(df.describe(include='all'))

# -------- Homework 2 --------
print("\n\nHomework 2\n")

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
              'Sales': [5000, 6000, 7500, 8000],
              'Expenses': [3000, 3500, 4000, 4500]}
sales_df = pd.DataFrame(sales_data)

# 2. Max sales and expenses
print("Max Sales:", sales_df['Sales'].max())
print("Max Expenses:", sales_df['Expenses'].max())

# 3. Min sales and expenses
print("Min Sales:", sales_df['Sales'].min())
print("Min Expenses:", sales_df['Expenses'].min())

# 4. Average sales and expenses
print("Average Sales:", sales_df['Sales'].mean())
print("Average Expenses:", sales_df['Expenses'].mean())

# -------- Homework 3 --------
print("\n\nHomework 3\n")

expenses_data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
                 'January': [1200, 200, 300, 150],
                 'February': [1300, 220, 320, 160],
                 'March': [1400, 240, 330, 170],
                 'April': [1500, 250, 350, 180]}
expenses_df = pd.DataFrame(expenses_data)

# Set index to 'Category'
expenses_df.set_index('Category', inplace=True)

# 2. Max expense for each category
print("Max expense per category:")
print(expenses_df.max(axis=1))

# 3. Min expense for each category
print("\nMin expense per category:")
print(expenses_df.min(axis=1))

# 4. Average expense per category
print("\nAverage expense per category:")
print(expenses_df.mean(axis=1))
