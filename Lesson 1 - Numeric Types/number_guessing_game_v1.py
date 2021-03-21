from random import randint

def guessing_game():
    answer = randint(0, 100)
    print("Guess my number")
    
    while True:
        user_guess = int(input("What is your guess: "))
        
        if user_guess == answer:
            print(f'Correct! My number is {user_guess}')
            break
        
        if user_guess < answer:
            print(f'Your guess {user_guess} is too low.')
        
        else:
            print(f'Your guess {user_guess} is too high.')


guessing_game()
    