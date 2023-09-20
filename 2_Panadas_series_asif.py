import pandas as pd

# Pandas Series

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# Labels

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar[0])

# Create Labels

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# Another example

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar["y"])

# Key/Value Objects as Series

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# Another example

calories = {"day1": 320, "day2": 210, "day3": 120}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)

# DataFrames

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)





