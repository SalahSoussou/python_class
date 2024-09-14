name = "Salah"
age = 25
rank = 10

print("My Name is : %s" % name)#My Name is : Salah

print("My Name is : %s and My Age is : %d" % (name,age))
#My Name is : Salah and My Age is : 25

print("My Name is : %s and My Age is : %d and Rank is %f" % (name,age,rank))
# My Name is : Salah and My Age is : 25 and Rank is 10.000000

# %s => String
# %d => Number
# %f => Float

print("My Rank is %f" % rank) #10.000000
print("My Rank is %.2f" % (rank)) #10.00

# =============================================
### Sring Formating New Version
# =============================================

print("My Name is : %{} and My Age is : {} and Rank is {}".format(name,age,rank))
print("My Name is : %{:s} and My Age is : {:d} and Rank is {:f}".format(name,age,rank))


myMoney = 58387684993

print("My Money is: {:d}".format(myMoney)) #58387684993
print("My Money is: {:_d}".format(myMoney)) #58_387_684_993
print("My Money is: {:,d}".format(myMoney)) #58,387,684,993


# =============================================
### Sring Formating New Version  3.6+
# =============================================

myNam = "Salah"
old = 25

print("my Name Is {maNam} I'm {old} old") #my Name Is {maNam} I'm {old} old
print(f"my Name Is {myNam} I'm {old} old") #my Name Is Salah I'm 25 old