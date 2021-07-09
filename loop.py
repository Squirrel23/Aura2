import os
os.system("cls")

# two types of loop 
## WHILE LOOP
i =  0
while i<=10:
    print(i)
    i = i +1
print("I am otside of loop")

i =  2      ##even no
while i<=100:
    print(i , end="\t")
    i = i +2
print()


i =  2      ##infinite loop
while i<=100:
    print(i , end="\t")


a=1
while a <=10:
    print(a)
    a = a+1

a=10
while a >0:
    print(a)
    a = a-1  

a = int(input("Enter the Number")) ##tables using loop
i = 1
while i <= 10:
    print(a , "*", i , "=" , a*i, ".\n")
    i = i + 1

a = 0     ##even no.
while a <=100:
    print(a)
    a = a +2

i=1        ####even no.
while i<=100:
    if i%2==0:
        print(i, end="\t")
    i=i+1

num=int(input("Enter number:")) #even no without using using i=2
i=0
while i<=num:
    if i%2==0:
        print(i)
    i=i+1

num=int(input("Enter number:")) #reverse even no.
i=2
while num>=i:
    if num%2==0:
        print(num)
    num=num-1

num=int(input("Enter number:")) #reverse
i=0
while num>=i:
    print(num)
    num=num-1

i = 1
while i<=100:
    if i%2==0 and i%5==0:
        print(i)
    i=i+1
    
i = 1
while i<=100:
    if i%2==0 and i%5!=0:
        print(i)
    i=i+1
print() 

##Calculating Factorial Method 1
a=int(input("Ente the number"))
i=1    
fact=1
while i <=a:
    if a!=0:
        fact = fact*i
    i= i+1
print(fact)

##Calculating Factorial Method 2
i=int(input("Ente the number"))
j=i-1
if i==0:
    print(1)
else: 
    while j>=1:
        if i!=0:
            i=i*j
        j=j-1
    print(i)

##Sum of series Method1
##1+2+3....n=
i=int(input("Ente the number"))
j=i-1 
while j>=1:
    i=i+j
    j=j-1
print(i)

##Sum of series Method2
n= int(input("enter the term"))
i = 1
sum = 0
while i<=n:
    sum = sum + i
    i = i + 1
print(sum)

##Sum Of Sqaures in series
##1^2+2^2+3^2....n^2=
n= int(input("enter the term"))
i = 1
sum = 0
while i<=n:
    sum = sum + i**2
    i = i + 1
print(sum)

#Maths Tables
num=int(input("Enter your nnumber"))
i=1
while i<=10:
    print(num,"*",i,"=",num*1)
    i = i+1

#5 +10+15+20
i=5
while i<=20:
    print(i,end="+")
    i=i+5
