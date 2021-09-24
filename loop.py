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

####################
## While 
def runwhile(i=0):
    while i < 6:
        i += 1
        if i == 3:
            continue
        if i == 5:
            break

        print(i)
    else:
        print('is more')

print("-"*10,"While loop","-"*10)
print("-----form 0") 
runwhile(0)

print("-----form 10") 
runwhile(10)