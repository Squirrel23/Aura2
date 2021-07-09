a=int(input("enter the number"))
i=20
while (1<=10):
print(i) ##indentation error

i=20
while (i<=10): #while condition is false
    pass  #block is passed
print(i)   ##i is 20 and is printed

i=5
while (i<=10):
    pass #infinite loop
print(i)  

i=5 #declaration statement
while (i<=10): #condition check statement
    pass
    i=i+1 #updation
print(i) #i= loop control variable

i=1  ##example of infinite loop
while i<2:
    pass
    print("a", end=",") 
print(i)

i=5
while (i<=10): #till i=10, condition remains true
    pass
    i=i+1  #loop terminates here after i=10+1
print(i) #ans 11










