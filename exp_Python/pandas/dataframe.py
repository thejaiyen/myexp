import pandas as pd

# DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
print("-"*10,"load data into a DataFrame object","-"*10)

df = pd.DataFrame(data)
print(df) 

#return one or more specified row with loc
print("-"*10,"return one or more specified row with loc (single)","-"*10)
print(df.loc[0]) 

print("-"*10,"return one or more specified row with loc (more)","-"*10)
print(df.loc[[0,2]]) 


#load data into a DataFrame object with index:
print("-"*10,"load data into a DataFrame object with index","-"*10)

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

#return one or more specified row with loc (index)
print("-"*10,"return one or more specified row with loc (index)","-"*10)
print(df.loc["day1"]) 