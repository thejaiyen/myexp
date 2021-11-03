l1 = ['10', '20', '30', '23', 'to', '25', '30', 'to', '40']
# l1 = ['10', '20', '30', '23',  '25', '30',  '40']
print (l1.count("to"))

x = 1
for i in range(l1.count("to")):
    y = l1.index("to",x)
    x = x + l1.index("to",x)


l2 = ['a','b','c']
l3 = ['1','2','3']

l2.extend(l3)
print(l2)