a = ["Welcome",50,3.14,3j+10,["A", "B", "C", "D"],("A", "B", "C", "D"),
    {"A":"a", "B":"b", "C":"c", "D":"d"},{'A', 'B', 'C', 'D'},range(6),
    frozenset({"apple", "banana", "cherry"}),True,b"Hello",bytearray(5),
    memoryview(bytes(5))]

def typeshow(income):
    print (income,'is',type(income))

# typeshow(a)
for i in a:
    typeshow(i)

# check type
print("-"*10,"check type","-"*10)
print( isinstance(a,str) )

# use in IF
print("-"*10,"use in IF","-"*10)
if(isinstance(a,str)):
    print ("yes")
else:
    print ("no")

#covert call Casting
print("-"*10,"covert","-"*10)
print( str(3) )
print( int(3) )
print( float(3) )