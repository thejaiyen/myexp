####################
#array in string ,call Slicing
# a[start:stop:step]
print("-"*10,"Slicing","-"*10)

a = " Hello form the other side"

o00 = a[1]
print( "o00 is",o00 )

o01 = a[5:]
print(  "o01 is",o01 )

o02 = a[:3]
print( "o02 is",o02 )

o03 = a[::4]
print( "o03 is",o03 )

####################
##Modify
print("-"*10,"Modify","-"*10)

a = " Hello form the other side"

#Split 
o1 = a.split(" ")
print ("o1 is",o1)
#Remove Whitespace
o2 = a.strip().split(" ")
print ("o2 is",o2)
#Replace 
o3 = a.replace("Hello", "Hi")
print ("o3 is",o3)

####################
##concatenate, or combine
print("-"*10,"combine","-"*10)

b = "Hi"
c = "bob"

print("b+c is",b+c) 

####################
##Format
print("-"*10,"Format","-"*10)

b = "Hi"
c = "bob"
#1
print("#1 say {} , {}".format(b,c))
#2
print("#2 {1} say {0}".format(b,c))
#3
print(f"#3 {b} say {c}")

##Escape Characters
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

##String functions
#https://www.javatpoint.com/python-strings