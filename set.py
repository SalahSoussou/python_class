mySet1 = {"salah",10,"python"}

print(mySet1)


# ==========================
#   set Methods
# ==========================

a = {1,2,3,4}

a.clear()

print(a) # set()


b = { "one","Tow","Three"}

c= {1,2,3}

print(b|c)  # {1, 2, 3, 'Tow', 'Three', 'one'}
print(b.union(c)) # {1, 2, 3, 'Tow', 'Three', 'one'}



c.add(4)
c.add(5)

print(c) # {1, 2, 3, 4, 5}


















