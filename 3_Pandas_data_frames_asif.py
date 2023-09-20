import  pandas as pd

# DataFrames

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data) # load data into a DataFrame object:

print(df) 

# Locate Row

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data) # load data into a DataFrame object:

print(df.loc[0])

# Another example

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data) # load data into a DataFrame object:

print(df.loc[[0, 1]])

# Named Indexes

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

# Locate Named Indexes

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df.loc["day2"])

# Load Files Into a DataFrame

df = pd.read_csv('data.csv')

print(df) 
