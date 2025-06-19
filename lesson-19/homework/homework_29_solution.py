
import pandas as pd
import sqlite3

# -------- Homework 1: Analyzing Sales Data --------
sales_df = pd.read_csv('task/sales_data.csv')

# 1. Group by Category
category_stats = sales_df.groupby('Category').agg(
    total_quantity=('Quantity', 'sum'),
    average_price=('Price', 'mean'),
    max_quantity=('Quantity', 'max')
)

# 2. Top-selling product in each category
top_products = sales_df.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top_products = top_products.sort_values(['Category', 'Quantity'], ascending=[True, False])
top_selling = top_products.groupby('Category').first().reset_index()

# 3. Date with highest total sales (quantity * price)
sales_df['Total'] = sales_df['Quantity'] * sales_df['Price']
date_sales = sales_df.groupby('Date')['Total'].sum().reset_index()
max_sales_date = date_sales.sort_values('Total', ascending=False).head(1)

# -------- Homework 2: Examining Customer Orders --------
orders_df = pd.read_csv('task/customer_orders.csv')

# 1. Customers with 20 or more orders
order_counts = orders_df.groupby('CustomerID').size().reset_index(name='order_count')
customers_20_plus = order_counts[order_counts['order_count'] >= 20]

# 2. Customers with avg price > $120
avg_price_per_customer = orders_df.groupby('CustomerID')['Price'].mean().reset_index()
high_value_customers = avg_price_per_customer[avg_price_per_customer['Price'] > 120]

# 3. Product totals, filter out quantity < 5
product_totals = orders_df.groupby('Product').agg(
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
).reset_index()
filtered_products = product_totals[product_totals['total_quantity'] >= 5]

# -------- Homework 3: Population Salary Analysis --------
# Read salary band data from Excel
salary_band_df = pd.read_excel('task/population salary analysis.xlsx')

# Connect to the database
conn = sqlite3.connect('task/population.db')
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

# Merge with salary band data
# Assume salary_band_df has columns: 'MinSalary', 'MaxSalary', 'Band'
def categorize_salary(salary):
    for _, row in salary_band_df.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return 'Unknown'

population_df['SalaryBand'] = population_df['Salary'].apply(categorize_salary)

# 1. General stats by salary band
band_stats = population_df.groupby('SalaryBand').agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()
total_population = population_df.shape[0]
band_stats['percentage'] = (band_stats['population_count'] / total_population) * 100

# 2. Stats by salary band and state
band_state_stats = population_df.groupby(['State', 'SalaryBand']).agg(
    population_count=('Salary', 'count'),
    average_salary=('Salary', 'mean'),
    median_salary=('Salary', 'median')
).reset_index()
state_totals = population_df.groupby('State').size().reset_index(name='state_total')
band_state_stats = pd.merge(band_state_stats, state_totals, on='State')
band_state_stats['percentage'] = (band_state_stats['population_count'] / band_state_stats['state_total']) * 100
