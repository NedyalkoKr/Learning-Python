from random import randint

def guessing_game():
    tries = 5
    answer = randint(0, 100)
    print("Guess my number")
    
    while True:
        try:
            user_guess = int(input("What is your guess: "), base=10)
            
            if tries == 0:
                print("No more tries left.")
                break
            
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
        except ValueError:
            raise ValueError("Invalid Input!")

guessing_game()
    