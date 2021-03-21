number = input("Enter a number(only integers): ")

if number.isdigit():
    number = int(number, base=10)
    print(1 + number)
