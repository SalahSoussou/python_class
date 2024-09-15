# ========================

myList = ["One","Tow",10,True]

print(myList) # ['One', 'Tow', 10, True]

print(myList[1]) #'Tow'

print(myList[1:]) # ['Tow', 10, True]

# -------------------
# -- Lists Methods --
# -------------------

#    append() =============================================

myList.append("Salah")

print(myList) # ['One', 'Tow', 10, True, 'Salah']

myList.append([3,5,"hello"])

print(myList) # ['One', 'Tow', 10, True, 'Salah',[3,5,"hello"]]




#    extend() =============================================

myFriends = ["salah", "simo","alaa"]
a= ["A","B"]


myFriends.extend(a)
print(myFriends) #  ['salah', 'simo', 'alaa', 'A', 'B']

#    remove() =============================================

myFriends.remove("A")

print(myFriends) #  ['salah', 'simo', 'alaa', 'B']


#    sort() =============================================

y =[1,120,2,7,3,-10,4]

y.sort()
print(y) # [-10, 1, 2, 3, 4, 7, 120]

y.sort(reverse=True)

print(y) # [120, 7, 4, 3, 2, 1, -10]

z = ["A","B","Z","O","L"]

z.sort()
print(z) #['A', 'B', 'L', 'O', 'Z']


#    reverse() =============================================

x = ["A","B","Z",11,4]
 
x.reverse()
print(x) #[4, 11, 'Z', 'B', 'A']

