# example of using functions
# each function encapsulate specific behaviour

# and one function can reuse another function 
# instead of implementing the same behaviour again

# the main purpose of using functions is code reusability

def nth_root(radiand, n):
    return radiand ** (1/n)


def ordinal_suffix(value):
    s = str(value)
    
    if s.endswith("1"):
        return f"{value}st"
    elif s.endswith("2"):
        return f"{value}nd"
    elif s.endswith("3"):
        return f"{value}rd"
    elif s.endswith("4"):
        return f"{value}th"
    elif s.endswith("5"):
        return f"{value}th"    
    elif s.endswith("6"):
        return f"{value}th"
    elif s.endswith("7"):
        return f"{value}th"
    elif s.endswith("8"):
        return f"{value}th"
    elif s.endswith("9"):
        return f"{value}th"
    return "th"

# demostrating function decomposition which is
# constructing more complex functions by reusing existing functions

def ordinal(value):
    return str(value) + ordinal_suffix(value)


def display_nth_root(radicand, n):
    # storing waht function returns in a local variable
    root = nth_root(radicand, n)
    message = f"The {ordinal(n)} root of {str(radicand)} is {str(root)}"
    print(message)


display_nth_root(64, 4)