mylist = ['value1', 'value2', 'value3']
print(mylist)
print(mylist[-1])

#a list can contain multiple data types

multiList = [3, 'string', True]

#using the list() constructor

mylist = list(('v1', 'v2'))

#Negative indexing applies
#Slicing rules apply
#Indexing starts from 0 
#Keyword 'in' can be used to check for an item 

print(mylist)

mylist[0] = 'v3'
print(mylist)

mylist[0:1] = ['v4', 'v5']
print(mylist)

mylist[0:2] = ['v6']
print(mylist)

mylist.insert(1, 'v7')
print(mylist)

#Add and Remove items 

mylist = ["apple", "banana", "cherry"]
extList = ["watermelon", "guava", "kiwi"]

mylist.append('watermelon')
print(mylist)

mylist.extend(extList)
print(mylist)

mylist.remove("apple")
print(mylist)

mylist.pop()
print(mylist)

del mylist[0]
print(mylist)

mylist.clear()
print(mylist)

mylist = ["apple", "banana", "cherry"]