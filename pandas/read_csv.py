import pandas as pd

df = pd.read_csv('data.csv')

# NaN is blank

#to_string() to print the entire DataFrame (all):
print("-"*10,"to_string()","-"*10)
print(df.to_string()) 

#print the entire DataFrame (summary):
print("-"*10,"print(df)","-"*10)
print(df) 

#printing the first rows of the DataFrame:
print("-"*10,"printing the first rows of the DataFrame","-"*10)
print(df.head())

print("-"*10,"printing the first 10 rows of the DataFrame","-"*10)
print(df.head(10))

#printing the last rows of the DataFrame:
print("-"*10,"printing the last rows of the DataFrame","-"*10)
print(df.tail())

print("-"*10,"printing the last 10 rows of the DataFrame","-"*10)
print(df.tail(10))


# information about the DataFrames 
print("-"*10,"information about the DataFrames ","-"*10)
print(df.info()) 