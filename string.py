a = " Hello form the other side"

#array in string
# a[start:stop:step]
o00 = a[1]
print( "o00 is",o00 )

o01 = a[5:]
print(  "o01 is",o01 )

o02 = a[:3]
print( "o02 is",o02 )

o03 = a[::4]
print( "o03 is",o03 )

#
o1 = a.split(" ")
print ("o1 is",o1)
#
o2 = a.strip().split(" ")
print ("o2 is",o2)