# 25 program for use of pandas library

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Select a column
print("\nAges:")
print(df['Age'])

# Add a new column
df['City'] = ['New York', 'Los Angeles', 'Chicago']
print("\nDataFrame with City column added:")
print(df)

print("\nPeople older than 25:")
print(df[df['Age'] > 25])

print("\nBasic statistics for Age:")
print(df['Age'].describe())
