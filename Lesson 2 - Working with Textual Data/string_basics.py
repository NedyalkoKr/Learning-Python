# using string data type to represent textual data

# representing string object using its literal form(notation)
# string is a sequence(collection) of unicode code points in PY3
# enclosed in a single or double quotes

print('Hello, World!')

# this is also a string object
print('1')

message = 'Hello, World!'
print(message)

# mixin quotes styles

print("You're the best teacher.")
print('You\'re the best teacher.')
print("You\'re the best teacher.")
print("Creating a startup takes a 'lot' of time, 'persistence'.")

# multiline string

text = """
This 
is
a
example
of very
long
multiline
string.
"""

# string as collection data type use indexes to map the position of each char in the string
# we can reference that index to get(retrive) individual chars

print(message[0])
print(message[1])
print(message[3])
print(message[-1])
print(message[len(message) - 1])

# using a index that dosent exist will cause PY to raise a error
# string object have a length attribute

print(message.__len__())

# but what we actualy will be doing is this

print(len(message))

# concatenating strings

word1 = "Hello,"
word2 = "World!"

phrase = word1 + " " + word2
print(phrase)

# formatting a string 

first_string = "{}, {}".format(word1, word2)
print(first_string)

second_string = "{0}, {1}".format(word1, word2)
print(second_string)

# string interpolation
third_string = f"{word1} {word2}"
print(third_string)