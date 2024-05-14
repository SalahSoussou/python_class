# --- Concatenation ---
a = "hello "
b = 'string'

print(a+b) #  hello string

myStr = 'String"test" end'

print(myStr) #  String"test" end

# Indexing (Access Item)

print(myStr[0]) #  Index [0]=> S
print(myStr[1]) #  Index [0]=> t
print(myStr[-1]) #  Index [-1]=> d  start from the end

# slicing ( Access Multiple Items )
# [start:end]
# [start:end:steps]

myString = "I Love Python"

print(myString[2:5]) # Lov
print(myString[2:6]) # Love
print(myString[:7]) # I Love
print(myString[7:]) # Python


print(myString[0::2]) # ILv yhn

# str Methods

myVar = "   Welcome to Linux Lite    "
print(len(myVar)) #  => 28

# strip()  rstrip()  lstrip()  =>  remove whitespace

print(myVar.strip())
print(myVar.rstrip())
print(myVar.lstrip())










