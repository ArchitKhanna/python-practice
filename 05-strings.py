print("hello")

#assign to a variable '' and "" are both valid
x = ' World!'

#concatenate
print ("Hello" + x)

#Typecast
y = str(2)
print(y)

#Multiline Strings with """ or '''
z = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(z)

#length function
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

#combine strings and numbers using format(). {0} use index values for many placeholders, to ensure the correct numbers are replaced
m = "This is room number {}"
n = 35
print(m.format(n))

#using escape characters
o = "This is for an \"escape\" character"
print(o)

#\n new line
#\\ backslash
#\t Tab
#\r carriage return
#\b backspace
#\f form feed
#\ooo octal value
#xhh hex value

#####################################################

g = "Believe"
print(g)

g = """This is a multiline string which
allows the python variable to store several 
lines of string together""" #Single quotes work too
print(g)

# Access strings like arrays
g = "Oranges"
print(g[0])

# Access strings using for loop
for s in "Mercedes":
    print(s)

# Length of a string
print(len(g))

# Check if a term is in a string
sent = "Luke this is your father"
print("this" in sent)

if "your" in sent:
    print("The word is present!")

print("something" not in sent)

if "something" not in sent:
    print("The word is not present")

# Slicing a string
print(g[1:4])
print(g[:5])
print(g[4:])
print(g[-6:-3])

# Modify strings
print(g.upper())
print(g.lower())

h = " The world is beautiful! "
print(h.strip()) # Remove whitespaces

print(h.replace("w", "W"))

print(h.split(" "))

# Concatenate strings
i = "Hello,"
j = " World!"
k = i+j
print(k)

# Using format to add numbers to strings
l = 2
m = 3
n = 1
order = "I would like {0} pizzas, {2} garlic bread and {1} lemon iced tea"
print(order.format(l,m,n))

# Using escape characters
p = "This is the \"plant\" I was talking about!"
print(p)
print("This is a \n new line character")
print("This is a \r return character")
print("This is a \t tab character")
print("This is a \b backspace character")
print("\115\056\142\123\117")

q="  heAthrow"
print(q.capitalize())
print(q.casefold())
print(q.count(q))
print(q.encode())
print(q.endswith("w"))
print(q.find("A"))
print(q.index("r"))
print(q.lstrip())