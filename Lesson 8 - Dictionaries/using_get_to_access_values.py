example_dict = {
    'key1': 'value1',
    'key2': 'Hello, World!',
    'key3': 10 + 23 * 9,
    'key4': bin(10),
    'key5': '',
    'key6': 'value1',
    'key7': 'value1',
    'key8': 'value1',
    'key9': 'value1',
}

print(example_dict.get('key1'))
print(example_dict.get('key10'))

# set default value with get()
# if key dosent exist in a dict

print(example_dict.get('key10', 'default'))

# if we dont provide a default py will return None
print(example_dict.get('key10')) # => None