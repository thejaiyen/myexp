import pandas as pd

# Pandas Series is like a column in a table

a = [1, 7, 2]

#load data into a Series:
print("-"*10,"Series is","-"*10)

myvar = pd.Series(a)
print(myvar)

#load data into a Series with index:
print("-"*10,"Series with index is","-"*10)

myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

#access an item in Series with index:
print("-"*10,"access an item in Series with index \"y\" is","-"*10)
print(myvar["y"])