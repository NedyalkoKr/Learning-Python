petko = {
    'first_name': 'petko',
    'last_name': 'petkov',
    'city': 'Burgas'
}

for key, value in petko.items():
    print(f'{key.title()}: {value.title()}')

print('\n')

maria = {
    'first_name': 'maria',
    'last_name': 'ivanova',
    'city': 'Varna'
}

for key, value in maria.items():
    print(f'{key.title()}: {value.title()}')

print('\n')

ivan = {
    'first_name': 'Ivan',
    'last_name': 'Petkov',
    'city': 'Sofia'
}

for key, value in ivan.items():
    print(f'{key.title()}: {value.title()}')

# or 

users = {
    'petko': {
        'first_name': 'petko',
        'last_name': 'petkov',
        'city': 'Burgas'
    },

    'maria': {
        'first_name': 'maria',
        'last_name': 'ivanova',
        'city': 'Varna'
    },

    'ivan': {
        'first_name': 'Ivan',
        'last_name': 'Petkov',
        'city': 'Sofia'
    }
}

for user_info in users.values():
    print('\n')
    for item, value in user_info.items():
        print(f'{item.title()}: {value.title()}')
