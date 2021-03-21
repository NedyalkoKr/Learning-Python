a = 5

while True:
    print(a)
    if a >= 2:
        print("Breaking out of the loop.")
        # break will jumps out of the most inner loop to the line after it
        break
    a -= 1

# or 

while True:
    response = input()
    if int(response) % 7 == 0:
        print(response)
        break