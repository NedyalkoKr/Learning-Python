# for loop in python corespond to for-each in other languages
# the purpose is to loop(iterate) over each item in a collection of items

for number in [1,2,3,4,5,6,7,8,9]:
    print(number)

numbers = range(0, 10)

for item in numbers:
    print(item)


for item in range(0, 10):
    print(item)


for char in "hello, world!":
    print(char)
    
cities = ["london", "new york", "paris", "oslo", "helsinki"]

for city in cities:
    print(city.capitalize())

employees = {
    "employee1": "petko",
    "employee2": "ivan",
    "employee3": "maria",
}

for employee in employees:
    print(f"{employee}", f"{employees[employee]}")