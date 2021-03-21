# list is a ordered collection(sequence) of objects
# lists are mutable
# lists are iterable

# creating list object using list literal form

numbers = [1,2,3,4,5,6,7,8,9]
fruits = ["apple", "orange", "pear"]

# each list item position is map to a index that allows to reference and retrive that item

print(numbers[0])
print(fruits[0])
print(numbers[-1])
print(fruits[-1])
print(numbers[2])
print(fruits[6])

# if we try to retrive item that dosen't exist python will raise IndexError

print(fruits[10])

# reassign list item

numbers[-1] = "9"
print(numbers)

# list methods

prices = []

# append single item at the end of the list
prices.append(1.99)

print(prices)

prices.append(2.99)

print(prices)

# using list() constructor to create list from other collections

print(list("hello, world!"))

# list() can be called on a collection only data type
# passing not-iterable object will raise a error

print(list(10))