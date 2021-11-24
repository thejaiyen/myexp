import pandas as pd

df = pd.read_json('data.json')

#to_string() to print the entire DataFrame (all):
print("-"*10,"to_string()","-"*10)
print(df.to_string()) 

#print the entire DataFrame (summary):
print("-"*10,"print(df)","-"*10)
print(df) 