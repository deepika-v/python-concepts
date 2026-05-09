"""
Python Pandas Concepts

This module demonstrates Pandas fundamentals:
- Series and DataFrame creation
- Data manipulation and cleaning
- Data selection and filtering
- Grouping and aggregation
- Merging and joining
- Time series handling
- Data visualization basics
"""

import pandas as pd
import numpy as np

# ============================================================================
# PANDAS SERIES
# ============================================================================

print("=" * 60)
print("PANDAS SERIES")
print("=" * 60)

# Creating Series from list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print(f"Series from list:\n{series}")
print(f"Type: {type(series)}")

# Series with custom index
fruits = pd.Series([100, 200, 150, 300], index=['apple', 'banana', 'orange', 'grape'])
print(f"\nFruits series:\n{fruits}")
print(f"Index: {fruits.index.tolist()}")
print(f"Values: {fruits.values}")

# Accessing elements
print(f"Apple: {fruits['apple']}")
print(f"First element: {fruits.iloc[0]}")
print(f"Last element: {fruits.iloc[-1]}")

# ============================================================================
# DATAFRAME CREATION
# ============================================================================

print("\n" + "=" * 60)
print("DATAFRAME CREATION")
print("=" * 60)

# From dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['NYC', 'LA', 'Chicago', 'Houston'],
    'Salary': [50000, 60000, 70000, 55000]
}

df = pd.DataFrame(data)
print(f"DataFrame from dictionary:\n{df}")
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Index: {df.index.tolist()}")

# ============================================================================
# DATAFRAME OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("DATAFRAME OPERATIONS")
print("=" * 60)

# Basic info
print(f"DataFrame info:")
print(df.info())

print(f"\nDescriptive statistics:\n{df.describe()}")

# Column operations
print(f"\nMean salary: ${df['Salary'].mean():.2f}")
print(f"Max age: {df['Age'].max()}")
print(f"Unique cities: {df['City'].unique()}")

# ============================================================================
# DATA SELECTION AND FILTERING
# ============================================================================

print("\n" + "=" * 60)
print("DATA SELECTION AND FILTERING")
print("=" * 60)

# Column selection
print("Names column:")
print(df['Name'])

print("\nMultiple columns:")
print(df[['Name', 'Age']])

# Row selection
print("\nFirst row:")
print(df.iloc[0])

print("\nRows 1-2:")
print(df.iloc[1:3])

# Conditional filtering
print("\nPeople over 28:")
over_28 = df[df['Age'] > 28]
print(over_28)

print("\nPeople in NYC or LA:")
nyc_la = df[df['City'].isin(['NYC', 'LA'])]
print(nyc_la)

print("\nHigh earners (salary > 55000):")
high_earners = df[df['Salary'] > 55000]
print(high_earners)

# ============================================================================
# DATA CLEANING
# ============================================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Create DataFrame with missing data
data_with_nulls = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
}
df_nulls = pd.DataFrame(data_with_nulls)
print(f"DataFrame with nulls:\n{df_nulls}")

# Check for nulls
print(f"\nNull values:\n{df_nulls.isnull()}")
print(f"Null count per column:\n{df_nulls.isnull().sum()}")

# Drop nulls
df_dropped = df_nulls.dropna()
print(f"\nAfter dropping nulls:\n{df_dropped}")

# Fill nulls
df_filled = df_nulls.fillna(df_nulls.mean())
print(f"\nAfter filling with mean:\n{df_filled}")

# ============================================================================
# GROUPING AND AGGREGATION
# ============================================================================

print("\n" + "=" * 60)
print("GROUPING AND AGGREGATION")
print("=" * 60)

# Create larger dataset
sales_data = {
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'Sales': [100, 150, 200, 250, 120, 180]
}
df_sales = pd.DataFrame(sales_data)
print(f"Sales data:\n{df_sales}")

# Group by single column
print(f"\nSales by product:\n{df_sales.groupby('Product')['Sales'].sum()}")

# Group by multiple columns
print(f"\nSales by product and region:\n{df_sales.groupby(['Product', 'Region'])['Sales'].sum()}")

# Multiple aggregations
print(f"\nMultiple aggregations by product:")
grouped = df_sales.groupby('Product')['Sales'].agg(['sum', 'mean', 'count', 'std'])
print(grouped)

# ============================================================================
# MERGING AND JOINING
# ============================================================================

print("\n" + "=" * 60)
print("MERGING AND JOINING")
print("=" * 60)

# Create two DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Score': [85, 92, 78, 88]
})

print(f"DataFrame 1:\n{df1}")
print(f"\nDataFrame 2:\n{df2}")

# Inner join (default)
inner_join = pd.merge(df1, df2, on='ID', how='inner')
print(f"\nInner join:\n{inner_join}")

# Left join
left_join = pd.merge(df1, df2, on='ID', how='left')
print(f"\nLeft join:\n{left_join}")

# Outer join
outer_join = pd.merge(df1, df2, on='ID', how='outer')
print(f"\nOuter join:\n{outer_join}")

# ============================================================================
# TIME SERIES
# ============================================================================

print("\n" + "=" * 60)
print("TIME SERIES")
print("=" * 60)

# Create date range
dates = pd.date_range('2023-01-01', periods=10, freq='D')
print(f"Date range: {dates[:5]}...")

# Create time series data
ts_data = pd.DataFrame({
    'Date': dates,
    'Value': np.random.randn(10)
})
ts_data.set_index('Date', inplace=True)
print(f"\nTime series data:\n{ts_data.head()}")

# Resampling
monthly_data = ts_data.resample('2D').mean()
print(f"\nResampled (2-day mean):\n{monthly_data}")

# ============================================================================
# DATA VISUALIZATION BASICS
# ============================================================================

print("\n" + "=" * 60)
print("DATA VISUALIZATION BASICS")
print("=" * 60)

# Create sample data for plotting
plot_data = pd.DataFrame({
    'x': range(10),
    'y': np.random.randn(10),
    'category': ['A', 'B'] * 5
})

print("Sample data for plotting:")
print(plot_data.head())

# Basic plotting (requires matplotlib)
try:
    import matplotlib.pyplot as plt

    # Line plot
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.plot(plot_data['x'], plot_data['y'])
    plt.title('Line Plot')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Scatter plot
    plt.subplot(2, 2, 2)
    plt.scatter(plot_data['x'], plot_data['y'])
    plt.title('Scatter Plot')

    # Bar plot
    plt.subplot(2, 2, 3)
    means = plot_data.groupby('category')['y'].mean()
    plt.bar(means.index, means.values)
    plt.title('Bar Plot')

    # Histogram
    plt.subplot(2, 2, 4)
    plt.hist(plot_data['y'], bins=5)
    plt.title('Histogram')

    plt.tight_layout()
    plt.savefig('pandas_plots.png', dpi=100, bbox_inches='tight')
    plt.close()
    print("Plots saved to 'pandas_plots.png'")

except ImportError:
    print("Matplotlib not available for plotting")

# ============================================================================
# READING AND WRITING DATA
# ============================================================================

print("\n" + "=" * 60)
print("READING AND WRITING DATA")
print("=" * 60)

# Create sample data
sample_df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NYC', 'LA', 'Chicago']
})

# Save to CSV
sample_df.to_csv('sample_data.csv', index=False)
print("Data saved to 'sample_data.csv'")

# Read from CSV
read_df = pd.read_csv('sample_data.csv')
print(f"\nData read from CSV:\n{read_df}")

# Save to Excel (if openpyxl available)
try:
    sample_df.to_excel('sample_data.xlsx', index=False)
    print("Data saved to 'sample_data.xlsx'")
except ImportError:
    print("openpyxl not available for Excel export")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Series: 1D labeled array, DataFrame: 2D labeled data structure
2. Use .iloc[] for position-based indexing, .loc[] for label-based
3. Boolean indexing: df[df['column'] > value]
4. Group operations: df.groupby('column').agg(['sum', 'mean', 'count'])
5. Merge/join: pd.merge(df1, df2, on='key', how='inner/left/outer')
6. Handle missing data: .isnull(), .dropna(), .fillna()
7. Time series: pd.date_range(), .resample()
8. I/O operations: .to_csv(), .read_csv(), .to_excel()
9. Visualization: Built-in plotting with matplotlib
10. Data cleaning and transformation are core strengths
""")
