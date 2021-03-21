# dictionary is a data type that allows to map key to a value
# or to store data in key-value form
# they are widley used in python and django
# also are known as maps or associative arrays in other languages

# creating new dictionary using literal notation

dict1 = {
    "key1": "value1",
    "key2": "value2",
}

print(dict1)

# keys has to be unique, values not
# in ths example PY will use the last repeating key
dict2 = {
    "key1": "value1",
    "key1": "another value",
}

print(dict2)

# retrive dict values
print(dict1["key1"])

# or set existing key to map a diff object(data)
dict1["key1"] = "new value"
print(dict1["key1"])

# add new key-value pair
dict1["key3"] = "value3"
dict1["key4"] = "value4"

print(dict1)