print("hello")
x = ' World!'
print ("Hello" + x)
y = str(2)
print(y)

#Multiline Strings with """ or '''

z = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(z)

#length
print(len(x))

#access characters of a string as an array
print(x[1])

#loop through the string one character at a time
for a in 'banana':
    print(a)

b = "banana"

#check for a phrase or word
if 'ba' in b:
    print("Present")

if 'te' not in b:
    print("Absent")

#slicing a string (negative indexing is valid)
print(x[1:4])
print(x[:4]) #from start
print(x[1:]) #to end 

#Modifying strings 
print(x.upper()) #upper case
print(x.lower()) #lower case
print(x.strip()) #remove whitespace
print(x.replace("!","s")) #replace a character or phrase
print(x.split(" ")) #split string at the separator