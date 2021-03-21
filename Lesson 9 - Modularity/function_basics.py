# defining a new function

# x is the input to the function
# functions can accept one, or more or none parameters
# these parameters represent the initial data the function will use
# internaly

def square(x):
    # returning the output of a function
    return x * x

print(square(5))

# we can choose to bind parameters to local variables
# but because our parameter(s) are used as local variables 
# adding anoter name as alias to a parameter is not nessesery

def square_again(x):
    param_x = x
    output = param_x * param_x
    return output

print(square_again(5))

# in alsmost all cases functions will return single output
# if we are not explicitly using the return keyword
# function will implicitly return None

def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")


output = even_or_odd(2)
print(output is None)

# its better to use return statement

def nth_root(radicand, n):
    return radicand ** (1/n)

print(nth_root(16, 2))