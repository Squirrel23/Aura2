#chapter 2
if 1:
    print("i am in if")
else:
    print("i am not in if")


if 0:
    print("i am in if")
else:
    print("i am not in if")
    
    
if -2:
    print("i am in if")
else:
    print("i am not in if")
    
    
if 0:   #0 equivalent to false
    print("0")
if 1:
    print("1")
if 2:
    print("2")    
if 3:
    print("3")    
else:
    print("i am in else")
    
if 0:
    print("0")
elif 1:
    print("1")
elif 2:
    print("2") 
elif 3:
    print("3")
else:
    print("I am in else")
    
a=10
if a<5:
    if a>3:
        print("1")
    else:
        print("2")
else:
    print("5")
    
a=4
if a<5:
    if a>3:
        print("1")
    else:
        print("2")
else:
    print("5")
    
a=3
if a<5:
    if a>3:
        print("1")
    else:
        print("2")
else:
    print("5")
    
a=5
if a<3:
    print("1")
else:
    print("2")
print("3")

a=5
if a<3:
    print("1")
else:
    print("2")
print("3")

##16/06/2021
a ="computer"
print("o" in a) ###this is a memberspip operator
print("om" in a)
print("op" in a)


a = "10"
b = "10"
c = a
print(a is b) ###this is identity operator
print(a is b)

a=input("enter letter:")
if a in {'a', 'e' , 'o' , 'u'}:
    print("vowel")
else:
    print("consonant")

a=input("enter letter:")
if a in "aieou":
    print("vowel")
else:
    print("consonant")

a=input("enter letter:")
if a=='a':
    print("vowel")
elif a=='e':
    print("vowel")
elif a=='i':
    print("vowel")
elif a=='o':
    print("vowel")
elif a=='u':
    print("vowel")
else:
    print("consonant")

a=input("enter letter:")
if a=='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("vowel")
else:
    print("consonant")

a = True
b = False
b = a==b
if a:
    print("1")
else:
    print("2")

### ASSIGMENT ON IF ELSE
##Q1
a=int(input("enter first number:\t"))
b=int(input("enter second number:\t"))
if a>b:
    print(a,"is greater than",b)
else:
    print(b,"is greater than",a)
print()

##Q2
a=int(input("enter first number:\t"))
b=int(input("enter second number:\t"))
c=int(input("enter third number:\t"))
if a>b:
    if a>c:
        print(a,"is greatest")
    else:
        print(c,"is greatest")
else:
    print(b,"is greatest")
print()

##Q3
a=int(input("enter you rnumber:\t"))
if a<0:
    print('nagative')
elif a>0:
    print('positive')
else:
    print('zero')
print()

##Q4
a=int(input("enter the number:\t"))
if a%5==0 and a%11==0:
    print("divisible by 5 and 11")
else:
    print("not divisible by 5 and 11")
print()

##Q5
a=int(input("enter the number:\t"))
if a%2==0:
    print("Even")
else:
    print("Odd")
print()

##Q6
a=int(input("enter year:\t"))
if a%4==0:
    print("Leap Year")
else:
    print("Not a Leap Year")
print()

##Q7
a=input("enter a character:\t")
if a in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZ":
    print(a,"is an Alphabet")
else:
    print(a,"is not an Alphabet")
print()

##Q8
a=input("enter an Alphabet:\t")
if a in "aeiou":
    print("Vowel")
else:
    print("Consonant")
print()

##Q9
a=input("enter an Alphabet:\t")
if a in "abcdefghijklmnpqrstuvwxyz":
    print("Lower Case")
else:
    print("Upper Case")
print()

##Q10
a=int(input("Enter Week No, :\t"))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednesday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
else:
    print("Sunday")
print()


a=4
if a<1:
    print("a")
if 1<a<5:
    print("a")
if a>5:
    print("a")

a=4
if a<1:
    print("a")
elif 1<a<5:
    print("a")
elif a>5:
    print("a")

#nested if
P=int(input("enter your marks of P"))
C=int(input("enter your marks of C"))
M=int(input("enter your marks of M"))
#P=50, M=90, C=70
if P<50 and M<90 and C<70:
    print("Your Physics, Maths, Chemistry marks is not up to the mark.")
elif P<50 and M<90 or M<90 and C<70 or P<50 and C<70:
    print("")
else:
    if P>50:
        if C>70:
            if M>90:
                print("Science Side")
            else:
                print("Your maths marks is not up to the mark.")
        else:
            print("Your Chemistry marks is not up to the mark.")
    else:
        print("Your Physics marks is not up to the mark.")