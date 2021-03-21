# general format of a while loop

while "using true condition":
    pass

while True:
    pass

# implicit type casting to a boolean object
# but this is NOT accepted pattern 
# just use True as conditon to start the loop

while "Hello":
    pass

while 1:
    pass

a = 5
while a >= 1:
    print(a) 
    a -= 1

# another way we can write is

a = 5

while c != 0:
    print(a) 
    a -= 1

# we can write also like this
# but in python is better to be explicit than implicit like here
# (we are assuming that a is True) we don't check it explicilty

a = 5

while a:
    print(a) 
    a -= 1