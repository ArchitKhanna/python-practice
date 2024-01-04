a = 10
A = 5
b = 20
c = -10
r = "archit"

print(a)
print(b)
print(c)
print("addition of a and b is: ", a+b)
print("addition of a and c is: ", a+c)
print("addition of b and c is: ", b+c)
print("addition of a,b,c is: ", a+b+c)
print(A+a)
print(r)

d = str(3)
e = ' is'
E = ' is not'
f = " a number"
g = d+e+f
h = float(2)

print(r+E+f)
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

# Unpack

names = ["archit", "dhwani", 'vidhi', 'malhar']
s,t,u,v = names
print(names)
print(s,t,u,v)
print(s)
print(t)
print(u)
print(v)
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

def inside2():
    print(a)

def outside2():
    a=5
    print(a)

def overwrite2():
    global b
    b = 16

outside()
outside2()
inside()
inside2()
overwrite()
overwrite2()
print(a)
print(b)