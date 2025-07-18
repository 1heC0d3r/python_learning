# Import the random module to generate random numbers
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)

# Start an infinite loop so the user can keep guessing
while True:
    # Ask the user to guess a number and convert it to integer
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if guess == random_number:
        print("You guessed right!")
        break # Exit the loop if the guess is correct
    else:
        # if the guess is wrong, prompt to try again
        print("You guessed wrong. Try again!")