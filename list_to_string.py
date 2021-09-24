### Converd list to string
a = ["a","v","s","S",'q']
b = [1,'a',2,'b',3,'c']
c = [1,2,3,4,5]


##### for loop
def list2str(come):
    out = ''
    for i in come:
        out += i
    return out 

# print(list2str(c))
try:
    print(list2str(c))
except Exception as e: print(e)