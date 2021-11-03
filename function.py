def fuc1(agg1,agg2 = False):
    print("agg1 is",agg1)
    print("agg2 is",agg2)

####################
### with 1 agreement
print("-"*10,'fuc1("Hi")',"-"*10)

fuc1("Hi")

####################
### with 2 agreement
print("-"*10,'fuc1("Yo",True)',"-"*10)

fuc1("Yo",True)


########################################
### function ,return
def fuc2(agg1,agg2):
    return agg1+agg2

print("-"*10,'fuc2(1,2)',"-"*10)

print (fuc2(1,2))