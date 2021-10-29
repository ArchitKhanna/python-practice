myTuple = ("value1","value2","value3")

for a in range(len(myTuple)):
    print(myTuple[a], a)

oneTuple = ("value1",)

mixTuple = (1, "value2", True)
print(mixTuple[-2])

myTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(myTuple[1:4])

if "kiwi" in myTuple:
    print(True)

if "kiwi" not in myTuple:
    print(True)
else:
    print(False)

x = ("apple", "banana", "cherry")
y = list(x)
y[0] = "kiwi"
x = tuple(y)
print(x)

z = ("grapes",)
x += z
print(x)

#unpacking
(v1, v2, v3, v4) = x
print(v4)

#Multiply
bigTuple = x * 2
print(bigTuple)