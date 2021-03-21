# control flow statements(conditional statements)
# allows to branch execution based on the value of evaluated boolean expression
# used as a condition

# if statement

if "something is True":
    print("Then do this.")

if True:
    print("Its True!")
    
# in reality there is no need to explicitly check if something is False
# better logic is to check if something is True and if is not then is False

if False:
    pass

# py will implicilty convert(cast) none boolean object used as condition to bool object
# if True PY will move inside the conditional block

if 5 > 2:
    print("Its bigger!")

# using explicit bool() is not done in practice because of PY implicit bool casting

if bool(5 > 2):
    pass

# if-else

h = 42

if h > 50:
    print("Greater than 50")
else:
    print("50 or smaller")

# if-elif

if h > 50:
    print("Greater than 50")
elif h < 50:
    print("50 or smaller")

# if-elif-else

if h > 50:
    print("Greater than 50")
elif h < 50:
    print("50 or smaller")
else:
    print("They are equal!")