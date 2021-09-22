a = "Welcome"
b = 50
c = 3.14
d = 3j+10
e = ["A", "B", "C", "D"]
f = ("A", "B", "C", "D")
g = {"A":"a", "B":"b", "C":"c", "D":"d"}
h = {'A', 'B', 'C', 'D'}

def typeshow(income):
    print (income)
    print (type(income))
    print("-"*20)

typeshow(a)
typeshow(b)
typeshow(c)
typeshow(d)
typeshow(e)
typeshow(f)
typeshow(g)
typeshow(h)


# check type
print("-"*40)
print( isinstance(a,str) )

# use in IF
print("-"*40)
if(isinstance(a,str)):
    print ("yes")
else:
    print ("no")