# Pandas Introduction and Operations

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("========== PANDAS SERIES & DATAFRAME ==========\n")

# Create Series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)

print("Pandas Series:")
print(series)

# Create DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22]
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\n========== DATA INDEXING & SELECTION ==========\n")

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}

df = pd.DataFrame(data)

print("Selecting rows with index 1 and 3:")
print(df.iloc[[1, 3]])

print("\n========== HANDLING MISSING DATA ==========\n")

# Data with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 10, 20, np.nan, 50],
    'C': ['foo', 'bar', 'baz', 'qux', 'quux']
}

df_missing = pd.DataFrame(data)

print("Original DataFrame:")
print(df_missing)

# Fill missing values
df_filled = df_missing.fillna(0)

print("\nDataFrame after filling missing values with 0:")
print(df_filled)

print("\n========== MERGING & JOINING ==========\n")

# First DataFrame
df1 = pd.DataFrame({
    'key': ['A', 'B', 'C', 'D'],
    'value1': [1, 2, 3, 4]
})

# Second DataFrame
df2 = pd.DataFrame({
    'key': ['B', 'D', 'E', 'F'],
    'value2': ['foo', 'bar', 'baz', 'qux']
})

# Inner Join
inner_join = pd.merge(df1, df2, on='key', how='inner')

print("Inner Join:")
print(inner_join)

# Left Join
left_join = pd.merge(df1, df2, on='key', how='left')

print("\nLeft Join:")
print(left_join)

print("\n========== DATA VISUALIZATION ==========\n")

# Visualization DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'Score': [85, 72, 88, 95, 78]
}

df_chart = pd.DataFrame(data)

print("Displaying Bar Chart...")

# Plot bar chart
df_chart.plot(kind='bar', x='Name', y='Score', legend=None)

plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Student Scores')

plt.show()