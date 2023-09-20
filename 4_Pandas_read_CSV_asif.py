import pandas as pd 

# Read CSV Files

df = pd.read_csv('data.csv')

print(df.to_string())

# Another example

df = pd.read_csv('data.csv')

print(df)

# max_rows

print(pd.options.display.max_rows)

# Another example

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)




