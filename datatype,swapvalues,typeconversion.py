#Chapter 1'''

print("Hello World")
print("This is my first python program\n")

##Data Types
print("\n\t\t data types") 
ba=15
bA=True
bb=10.5
bc=15j
bd='22'
be=["apple", "banana", "cherry"]
bg=("apple", "banana", "cherry")
bh={"apple", "banana", "cherry"}
bf={"name" : "John", "age" : 36}
bx=None
print(type(ba))
print(type(bA))
print(type(bb))
print(type(bc))
print(type(bd))
print(type(be))
print(type(bg))
print(type(bh))
print(type(bf))
print(type(bx))

  
##Swap Values
 ###Method1: using third variable
na=int(input("The value of na is:"))
nb=int(input("The value of nb is:"))
nc=na
na=nb
nb=nc
print("The value of na is:",na)
print("The value of nb is:",nb)
 
###Method2: not using third variable
oa=int(input("\nThe value of oa is:"))
ob=int(input("The value of ob is:"))
oa,ob=ob,oa
print("The value of oa is:",oa)
print("The value of ob is:",ob)

##Explicit Type conversion
a=5
b=10
c=a+b
print(type(c))
c=float(a+b)
print(type(c))
 
##Implicit Type Conversion
a=5.5
b=10
c=a+b
print(type(c))

 
