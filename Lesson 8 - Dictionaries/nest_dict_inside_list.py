alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 15}
alien_2 = {'color': 'blue', 'points': 50}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

for dict_key1, dict_key2 in aliens:
    print(alien_0[dict_key1], alien_0[dict_key2])
    print(alien_1[dict_key1], alien_1[dict_key2])
    print(alien_2[dict_key1], alien_2[dict_key2])


users = [
    user1: {
        'firts_name': '',
        'last_name': '',
        'age': '',
        'email': '',
        'password': ''
    },

    user2: {
        'firts_name': '',
        'last_name': '',
        'age': '',
        'email': '',
        'password': ''
    },
]