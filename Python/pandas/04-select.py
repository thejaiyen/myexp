import pandas as pd

boxes = {'Color': ['Green','Green','Green','Blue','Blue','Red','Red','Red'],
         'Shape': ['Rectangle','Rectangle','Square','Rectangle','Square','Square','Square','Rectangle'],
         'Price': [10,15,5,5,10,15,15,5]
        }

# --------------------------------------------------------------
# Add data 
print("\n","-"*10,"Add data ","-"*10)

df = pd.DataFrame(boxes, columns= ['Color','Shape','Price'])

print (df)

# --------------------------------------------------------------
# Select Rows
# df.loc[df[‘column name’] condition]
print("\n","-"*10,"Select Rows ,Color = Green","-"*10)

select_color = df.loc[df['Color'] == 'Green']
print (select_color)

#  two conditions
##  can combine with Logical operator
#  & 	AND
#  |	OR
#  ^    XOR
#  ~ 	NOT
print("\n","-"*10,"Select Rows ,two conditions","-"*10)

color_and_shape = df.loc[(df['Color'] == 'Green') & (df['Shape'] == 'Rectangle')]
print (color_and_shape)


## addition
print("\n","-"*10,"df['Color'] == 'Green' show True,False","-"*10)

print ( df['Color'] == 'Green' )