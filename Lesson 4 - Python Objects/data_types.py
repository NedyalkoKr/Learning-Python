# python have dynamic and strong type system
# dynamic type system means that type of the object is resolved at runtime
# when programming is executed and we dont have to explicitly specify the 
# data type of each object

# for example in this function we dont have to set data type of the arguments
# a and b
# we can pass objects of any data type where + operator make sense

def add(a, b):
    return a + b

print(add(2, 10))
print(add(3.2, 5.2))
print(add("hello", "world!"))
print(add([1,2,3,4], [5,6,7,8]))

# strong type system means that PY will NOT implicitly convert(type cast) between 
# diff data types

# here PY will NOT implicilty cast int object to a string object
# and will raise a exeception
print(add("10", 1))

# one place where PY will perform implicit type converions is from non boolean object
# to bool in conditionals

a = 10

# here PY will impliclty cast integer 10 to True
if a:
    print(a)
