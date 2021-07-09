##input 
###A raised to power x
print("\n\t\t A raised to power x")
A=int(input("The value of base A is:"))
X=int(input("The value of degree X is:"))
E=A**X
print("The result is:",E)
 
###under root A
print("\n\t\t under root A")
AA=int(input("The value of A is:"))
XX=int(input("The value of x is:"))
EE=AA**(1/XX)
print("the Result is:",EE)

###Rectangle
print("\n\t rectangle")
x=int(input("The length of rectangle is:"))
y=int(input("The breadth of rectangle is:"))
p=x*y
print("The area of rectangle is:",p)
q=2*(x+y)
print("The perimeter of the rectangle is:",q)

###Cube
print("\n\tcube")
j=int(input("The length of edge of cube is:"))
k=6*j**2
print("The surface are of cube is:",k)
l=j**3
print("The volume of cube is:",l)

#Right Triangle
print("\n\tRight Triangle")
m=int(input("The height of right triangle is:"))
n=int(input("The base of right triangle is:"))
r=1/2*m*n
print("The Are of triangle is:",r)
ra=m+n+(m**2+n**2)**0.5
print("The perimeter of right triangle is:",ra)

###Scalene triangle
print("\n\t scalene triangle")
s=int(input("The length of first side of scalene triangle is:"))
t=int(input("The length of second side of scalene triangle is:"))
u=int(input("The length of third side of scalene triangle is:"))
v=(s+t+u)/2
w=(v-s)*(v-t)*(v-u)*v
z=w**0.5
print("The area of scalene triangle is:",z)

###Circle
print("\n\tcircle")
qa=int(input("The radius of circle is:"))
qb=2*22/7*qa
print("The circumference of circle is:",qb)
qc=22/7*qa**2
print("The area of circle is:",qc)  
  
###Quadratic Equation
print("\n\t quadratic equation")
aa=int(input("The coefficient of x^2 is:"))
ab=int(input("The coefficient of x is:"))
ac=int(input("The value of constant is:"))
ad=ab**2-4*aa*ac
ae=-ab+ad**0.5
af=-ab-ad**0.5
print("The value of first root is:",ae)
print("The value of second root is:",af)

###Change in mass unit
print("\n\n\t\t change in mass unit")
ra=int(input("\nThe value in metre is:"))
rb=ra*100
rc=ra/1000
print("The value in centimetre is:",rb)
print("The value in kilometre is:",rc)
 
###Change in temperatute units
sa=int(input("\nThe value in degree celsius is:"))
sb=sa*9/5+32
print("The value in degree fahrenheit is:",sb)

 