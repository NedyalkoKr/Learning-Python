# integers in python are represented as "unlimited" precision signed integers
# the size of the integer is limited by the size of the memory

# representing integers as literals

print(10)
print(-10)

# representing integers in binary notation

print(0b10)

# representing integers in octal notation

print(0o10)

# representing integers in hexadecimal notation

print(0x10)

# constructing integers by converting from none integer types to integers using 
# int() constructor

print(int(3.5))
print(int(-3.5))
# or converting string like integers
print(int("356"))

# be explicit and specifing the base
print(int(1000000, base=2))