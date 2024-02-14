import random

def new_game():
    difficulty = ""
    attempts = 0
    number = random.randrange(1, 101)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    else:
        print("Invalid input! Try again...")
        new_game()

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess == number:
            print("You guessed correctly!!!")
            attempts = 0
        elif guess > number:
            print("Too high!")
            attempts -= 1
            print(f"You have {attempts} attempts left.")
        else:
            print("Too low!")
            attempts -= 1
            print(f"You have {attempts} attempts left.")

    play_again = input("Would you like to play again? [y/n]")
    if play_again == "y":
        new_game()
    else:
        exit()

new_game()