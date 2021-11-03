####################
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
# a not in b
# a in []
# a is b
# a is not b

print("-"*10,"Condition in","-"*10)
print ('"abc" in "xabcy" is ', "abc" in "xabcy")
print ('"abc" in ["abcs","adasd","acs"] is',"abc" in ["abcs","adasd","acs"])

####################
## IF 
#1 if elif else
print("-"*10,"#1 if elif else","-"*10)

if False:
    print("#1")
elif True:
    print("#2")
else:
    print("#3")

##########
#2.1 if one line
print("-"*10,"IF #2.1 if one line","-"*10)

print ('High' if True else 'Low')

##########
#2.2
print("-"*10,"IF #2.2","-"*10)
x = 10
result = 'High' if x>10  else 'Low'
print(result)

##########
#2.3 if one line
print("-"*10,"IF #2.2","-"*10)

print (" print () if True else None") if True else None
print (" print () if False else None") if False else None