##Condition
# a == b
# a != b
# a < b
# a <= b
# a > b
# a >= b
# a and b
# a or b
# a in b
# a in []

print ("abc" in "xabcy")
print ("abc" in ["abcs","adasd","acs"])

## IF
#1
if True:
    print("#1")

#2
if False:
    print("#1")
elif True:
    print("#2")
else:
    print("#3")

#3 if one line
print ('High' if True else 'Low')

#3.2
x = 10
result = 'High' if x>10  else 'Low'
print(result)