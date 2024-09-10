#operations in python
#Arthmetic
#Assignment
#Comparison
#Logical
#Identity
#Membership
#Bitwise
#Ternary


#Arthetic Operators
#-> +,-,/,*, //, **, %
print(1+1)
print(4-5)
print(5*5)
print(25/5)
print(25//7) #int
print(5**3)
print(4%3)

#Assignment
#-> =, +=, -=, *=, /= , //=, **=
a = 10
print(a)
a += 1 #a = a+1
print(a)
a -= 1
print(a)
a *= 1
print(a)
a **=3
print(a)


#Comparison -> return Ture or False
# >, < , >=, <=, ==
print(4>5)
print(4<5)
print(4>=5)
print(4<=5)
print(4==5)
print(4==4)

#Logical
# and &, or |, not ! -> boolean True or False
b = True
c = True
d = False
print(b and c)
print(b or d)

#Membership -> Bool , in,  not in
e = [1,2,3,4,5]
print("membership")
print(3 in e)
print( 10 not in e)
print( 3 not in e)

#Identity is is not 
f = 10
g = f
h = 10
print("Identity")
print(f is g)
