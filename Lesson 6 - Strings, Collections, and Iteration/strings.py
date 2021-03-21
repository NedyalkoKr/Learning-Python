# string in python is a ordered sequence of unicode code points
# string is immutable, which means that once we construct the string we cannot change it

# ways to create(construct) a string 

# most common way is using literal string notation
print("hello, world")

# or bind to a variable
greeting = "Hello, World!"
print(greeting)

# or we use str() constructor which will try to convert(type cast) non-string object
# to a string object
# there is not logic to convert a string object if its already a string

print(str(10))
print(str(10 < 10))

# strings are enclosed(delimited) in single or double quotes

print("It's a good thing.")
print('It\'s a good thing.')
print("first" "second")

# string on many lines
# these quotation styles are used more often with docstrings

print(
"""
This 
is 
a
multiline
string.
"""
)


print(
'''
This
is 
a
multiline
string.
'''
)

# another approuch will be to use escape sequences

print("This\n is\n a\n multiline\n string.\n")
print("This is a \" in a string.")
print("This is a \' in a string.")
print('This is a \' in a string.')
print("This is a \" in a string.")
print("This is a \\ in a string.")
print("This is a \t in a string.")


# raw strings

path = r'C:\Users'
print(path)

# type casting to string objects

print(str(496))
print(str(6.02e32))

# because string is a ordered collection
# we can use index to access individual chars at specific position

s = "parrot"
print(s[0])
print(s[-1])

# some built-in string behaviours as methods
# string method is a another attribute we can call on string object
# these methods will NOT modify original string object(string is immutable) instead
# py will create a new string object

print("oslo".capitalize())
print("oslo".upper())

message = "Hello"
message.upper()

# original string object is NOT modified
print(message)