# float in python are represented as numbers with 53-bits of
# binary precision(which is equivalent to 15-16 significant digits after the decimal point)

# using float literals

print(3.125)
print(-3.125)

# using scientific notation to represent very small and very large floats

print(3e8)
print(1.161e-35)

# converting to float from a other non-floating types using float() constructor

print(float("1.618"))
print(float("nan"))
print(float("inf"))
print(float("-inf"))

# in expression where one of the operands is a float will always returns a float
# in this example python will first type cast(convert) integer 1 to a float and than evaluate the expression

print(3.0 + 1)