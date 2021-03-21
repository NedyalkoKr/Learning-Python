from random import randint

person = {
    'first_name': input('Your first name? '),
    'last_name': input('Your last name? '),
    'age': input('Age? '),
    'city': input('Your city? '),
}

print(f'{person['first_name']} {person['last_name']} is \
    {person['age']} years old and is from {person['city']}. ')
    

fav_number = {
    'petko': randint(1, 10),
    'maria': randint(1, 10),
    'ivan': randint(1, 10),
    'marko': randint(1, 10),
}

print(f'Petko favorite number is {fav_number['petko']} \
        Maria favorite number is {fav_number['petko']} \
        Ivan favorite number is {fav_number['ivan']} \
        Marko favorite number is {fav_number['marko']}')

glossary={
    'word1': 'description',
    'word2': 'description',
    'word3': 'description',
    'word4': 'description',
    'word5': 'description',
}
