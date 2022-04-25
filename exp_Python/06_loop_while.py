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