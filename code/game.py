# guess the number 
import random

# generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# set the number of guesses allowed
num_guesses = 7

# loop through each guess
for guess_num in range(1, num_guesses + 1):
    # get the player's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # check if the guess is correct
    if guess == secret_number:
        print("Congratulations, you guessed the number!")
        break

    # provide feedback to the player
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    # check if the player has run out of guesses
    if guess_num == num_guesses:
        print("Sorry, you ran out of guesses. The number was", secret_number)
