print(50/2//3%7*5)
print(50/-2//3%7*5)
print(50/-2//3%-7*5)
print(-50/-2//3%-7*5)

a,b,c,d=2,3,5,0
print(a and b or not c)
print(a or not b and c)
print(not d and d or b and a)
print(not a or not b and d or c)

a="1"
b=2
print(a*b)

x=2
y="56"
print(print((print(type(x))),type(y)),y*x)
#(print(type(x)) >> int
#(print(type(x))),type(y) >> None str
#(print((print(type(x))),type(y)),y*x) >> None 5656

x=23
print(type(print(print(id(print(type(print(id(x)))))))))
#(print(id(x))) == adress >> XXXXXXX
#(print(type(print(id(x))))) == type >> none type
#(print(id(print(type(print(id(x))))))) == id of (print(type(print(id(x))))) >> XXXXXXX
#(print(print(id(print(type(print(id(x)))))))) == None
#print(type(print(print(id(print(type(print(id(x))))))))) == type of (print(print(id(print(type(print(id(x)))))))) >>None type


#to print complex no.
a = complex(2,3)
print(a)
a = complex(8,3)
print(a)
a = complex(8,8)
print(a)