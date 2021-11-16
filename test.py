line = 'port trunk allow-pass vlan 99 to 100 188 289 to 291 301 310 to 312 3000 to 3001 3003 to 3004 3010'
line = line.split()
x = 1
z = 4
b = []
for i in range(line.count("to")):
    y = line.index("to",z)
    b.extend(line[z:y])
    for ii in range(int(line[y-1])+1,int(line[y+1])):
        b.append(str(ii))
    x = x + y
    z = y + 1
    print(i,y,x,b,z,int(line[y-1]),int(line[y+1]))
b.extend(line[z:len(line)])
# #print("b is ",b)
output[5] +=  ' '.join(b) + ' '