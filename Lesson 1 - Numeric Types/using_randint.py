from random import randint

# ex1

print(randint(a=-100, b=100))

# ex2 

random_numbers = []
for number in range(0, 11):
    random_numbers.append(randint(a=-100, b=100))    

print(random_numbers)