# string object have a built-in behaviour that we can access
# via predefined methods

# method is a function defined in a class and called on string object

message = 'Hello, World!'

print(message.title())
print(message.upper())

# count number of occurences of char l
print(message.count("l"))

# count number of occurences of word "Hello"
# in PY strings are case-sensitive
# which mean that hello and Hello are not the same string objects

print(message.count("Hello"))

# return the index where specific single char is located
print(message.find("H"))

# we can pass but it will return only the first index of the first char
print(message.find("ll"))

# will return -1
# so notice it dosen't raise a exception
print(message.find("h"))

# replace single char or a word in a string
# replace will return a new string object
# original string is NOT modified

message.replace("World", "Universe")
print(message)

new_message = message.replace("World", "Universe")
print(new_message)