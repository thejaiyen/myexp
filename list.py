####################
## List

l1 = ['10', '20', '30', '23', 'to', '25', '30', 'to', '40']
l2 = ['a','b','c']
l3 = ['1','2','3']
####################
## count
print("-"*10," .count()","-"*10)

print (l1)
print ("count 'to' in list :",l1.count("to"))

####################
## extend
print("-"*10," .extend()","-"*10)

print ("list 2 is",l2)
print ("list 3 is",l3)
l2.extend(l3)
print("extend list3 to list2 :",l2)

####################
## append
print("-"*10," .append()","-"*10)

print ("list 3 is",l3)
l3.append("4")
print("append '4' to list3 :",l3)