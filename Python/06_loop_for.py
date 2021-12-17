####################
## For
##########
#in range
print("-"*10,"For loop in range","-"*10)

for i in range(5):
    print(i)

##########
#in list
print("-"*10,"For loop in list","-"*10)

a = ["123","abc","c2s"]
for i in a:
    print(i)

##########
#in str
print("-"*10,"For loop in str","-"*10)

a = "1242"
for i in a:
    print(i)

##########
#for one line
print("-"*10,"for one line","-"*10)

# expression for item in iterable if condition == True
xx = [x for x in range(10) if x < 5]
print(xx)

##########
#end of for
print("-"*10,"end of for","-"*10)

for i in range(3):
    print(i)
else:
    print("end of for")

