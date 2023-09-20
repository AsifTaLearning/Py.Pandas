import pandas as pd

# Pandas - Analyzing DataFrames
# Viewing the Data

df = pd.read_csv('data.csv')

print(df.head(10))

# Another example

df = pd.read_csv('data.csv')

print(df.head())

# Another example

df = pd.read_csv('data.csv')

print(df.tail())






