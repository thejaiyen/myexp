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
## index
print("-"*10," .index()","-"*10)

print (l1)
print ("index 'to' in list :",l1.index("to"))

####################
## join with +
print("-"*10,"join with +","-"*10)

print ("list 2 is",l2)
print ("list 3 is",l3)
print("join with + :",l2+l3)

####################
## join with extend
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