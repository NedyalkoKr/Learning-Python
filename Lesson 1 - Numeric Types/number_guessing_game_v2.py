from random import randint

def guessing_game():
    tries = 5
    answer = randint(0, 100)
    print("Guess my number")
    
    while True:
        user_guess = input("What is your guess: ")
        
        if tries == 0:
            print("Game over!")
            break
        
        if user_guess.isdigit():
            user_guess = int(user_guess)
            
            if user_guess == answer:
                print(f'Correct! My number is {user_guess}')
                break
            
            if user_guess < answer:
                print(f'Your guess {user_guess} is too low.')
                print(f"You have left: {tries} tries")
                tries -= 1
                    
            else:
                print(f'Your guess {user_guess} is too high.')
                print(f"You have left: {tries} tries")
                tries -= 1
        else:
            print("Invalid Input!!!")
            break

guessing_game()