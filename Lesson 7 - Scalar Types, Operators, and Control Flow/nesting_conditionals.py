h = 42

if h > 50:
    print("Greater than 50")
else:
    # nesting is not a bad pattern, but in python is better to flat
    # than nested for readability
    if h < 20:
        print("Less than 20")
    else:
        print("Between 20 and 50")

# the same logic bu using flat structure

if h > 50:
    print("Greater than 50")
elif h < 20:
    print("Less than 20")
else: 
    print("Between 20 and 50")