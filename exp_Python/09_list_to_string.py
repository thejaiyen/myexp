####################
### Converd list to string
a = ["a","v","s","S",'q']
b = [1,'a',2,'b',3,'c']
c = [1,2,3,4,5]

####################
### for loop
print("-"*10,"for loop","-"*10)
def loop2str(come):
    out = ''
    try:
        for i in come:
            out += i
    except Exception as e:
        out = (f"{type(e).__name__} : {e} at line {e.__traceback__.tb_lineno}")
    return out 
print("a is",a)
print(loop2str(a))
print("b is",b)
print(loop2str(b))
print("c is",c)
print(loop2str(c))

####################
### .join()
print("-"*10,".join()","-"*10)
def join2str(come):
    out = ''
    try:
        out = " ".join(come)
    except Exception as e:
        out = (f"{type(e).__name__} : {e} at line {e.__traceback__.tb_lineno}")
    return out 
print("a is",a)
print("join is",loop2str(a))
print("b is",b)
print("join is",loop2str(b))
print("c is",c)
print("join is",loop2str(c))