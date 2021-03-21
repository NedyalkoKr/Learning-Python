favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f'{language.title()}')

# what if our dict contains many repeating values?

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'jen': 'python',
    'jen': 'python',
}

for language in set(favorite_languages.values()):
    print("The following languages have been mentioned:")
    print(f'{language.title()}')