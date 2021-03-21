scientist = {
    'einstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for name, info in scientist.items():
    print(f"\nScientist name: {user}")
    full_name = f"{user['first']} {info['last']}"
    location = user['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
