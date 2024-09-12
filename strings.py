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

mys = "@@@@Welcome to Linux Lite@@@"
print(mys.strip("@")) # => Welcome to Linux Lite

#
# mys.title()
#=> Return a version of the string where each word is titlecased.

# mys.capitalize()
#=> Return a capitalized version of the string.

# zfill
u, i, j = "1", "11", "111"
print(u) #=> 1
print(i) #=> 11
print(j) #=> 111

print(u.zfill(3)) #=> 001
print(i.zfill(3)) #=> 011
print(j.zfill(3)) #=> 111


#========================================
######  split()  ,  rsplit()  ####
#========================================


d = "I love python and php"

print(d.split())  #=> ['I', 'love', 'python', 'and', 'php']


c = "I-love-python-and-php"

print(c.split("-"))  #=> ['I', 'love', 'python', 'and', 'php']

print(c.split("-",2))  #=> ['I', 'love', 'python-and-php']

# rsplit()

print(c.rsplit("-",2))  #=> ['I-love-python', 'and', 'php']


#========================================
###### center() ####
#========================================

e = "Salah"

print(e.center(9,"@")) # @@Salah@@

# swapcase() 

g = "I Love Python"
h = "i lov python"

print(g.swapcase()) # i lOVE pYTHON
print(h.swapcase()) # I LOV PYTHON


# startswith()  vs  endswith()

print(g.startswith("I"))  #True
print(g.startswith("S"))  #False