a = 10
A = 5
b = 20
c = -10

print(a)
print(b)
print(c)
print("addition of a and b is: ", a+b)
print("addition of a and c is: ", a+c)
print("addition of b and c is: ", b+c)
print(A+a)

d = str(3)
e = ' is'
f = " a number"
g = d+e+f
h = float(2)

print(g)
print(type(a))
print(type(g))
print(h)

#Only alpha-numeric and underscore
#Cannot begin with a number
#Case sensitive
#Can begin with only a letter or underscore

i, j, k, = 1, 2, 3 #Multiple assignments
l, m, n, = 'first', "second",'third'
o = p = q = 10 #Multiple variables with same value

#global variables are declared outside a function while local are inside.
#a local variable can be made global by using the keyword global.

def outside():
    print(a)

def inside():
    a=2
    print(a)

def overwrite():
    global a 
    a = 22

outside()
inside()
overwrite()
print(a)