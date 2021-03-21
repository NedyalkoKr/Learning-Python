favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favorite_languages:
    print(name.title())

# like this one because is explicit

for name in favorite_languages.keys():
    print(name.title())

# using the key to get the values

for name in favorite_languages.keys():
    print(favorite_languages[name])

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name].title()
        print(f'{name.title()}, I see you love {language}')


for name in sorted(favorite_languages.keys()):
    print(f'{name.title()} thank you for taking the poll.')

    if 'erin' not in favorite_languages.keys():
        print(f'Only Erin didn\'t take the poll.')
