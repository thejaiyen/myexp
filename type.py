####################
##Type
print("-"*10,"Type","-"*10)

a = ["Welcome",50,3.14,3j+10,["A", "B", "C", "D"],("A", "B", "C", "D"),
    {"A":"a", "B":"b", "C":"c", "D":"d"},{'A', 'B', 'C', 'D'},range(6),
    frozenset({"apple", "banana", "cherry"}),True,b"Hello",bytearray(5),
    memoryview(bytes(5))]

for i in a:
    print (i,'is',type(i))

##########
# check type
print("-"*10,"check type","-"*10)

print( isinstance(a,str) )

##########
# use in IF
print("-"*10,"use in IF","-"*10)

if(isinstance(a,str)):
    print ("yes")
else:
    print ("no")

##########
#covert call Casting
print("-"*10,"covert","-"*10)

print("to str :\t", str(3) )
print("to int :\t", int(3) )
print("to float :\t", float(3) )