# Task
# Here’s a bigger challenge. Write the pseudocode for a program
# where the player and the computer trade places in the number
# guessing game. That is, the player picks a random number
# between 1 and 100 that the computer has to guess. Before you
# start, think about how you guess. If all goes well, try coding the
# game

           # Psuedocode
# Initialize a variable (limited_guess) equals to 3
# Initialize (player_number) Get a number from the player
# initialize a variable (computer_guess) equals to 0
# Initialize a variable (attempts) equals to 0

# While (limited_guess) is greater than 0
        # (computer_guess) Get random number from (1, 100)

        # (limited_guess) -= 1
        # (attempts) += 1

        # If (player_number) greater than (computer_guess)
            # Display guess higher
        # If (player_number) is less than (computer_guess)
            # Dispaly guess lower
        # Otherwise
            # Display computer you are correct
            # Display it took you (attempts) to guess right
            # Break
        # Re-initialize (computer_guess) equals to 0

# If (limited_guess) is equals to 0 and (player_number) not equals to (computer_gues)
    # Display lol after (attempts) tries you could not guess right

            # Implementation
import random
# Initializations
limited_guess = 3
computer_guess = 0
attempts = 0
player_number = 0

while player_number not in range(1, 101): # Ensure the player input is between 1 to 100
    # Get player input
    player_number = int(input("\nPlease enter a number from (1,100): "))

while limited_guess > 0: # If limited_guess is still greater than 0
    # Get computer gues
    computer_guess = random.randint(1,100)

    limited_guess -= 1 # Decrement limited_guess
    print("\nlimited_guess is: ", limited_guess)
    attempts += 1 # Increment attempts
    print("attempts is: ", attempts)
    print("player_number is: ", player_number)
    print("computer_guess is: ", computer_guess)

    if player_number > computer_guess: # Check if player_number is greater than computer_guess
        print("\nGuess higher")
    elif player_number < computer_guess: # Check if player_number is less than computer_guess
        print("\nGuess lower")
    else: # If player_number is equals to computer_guess
        print("\nYou are correct")
        print("It took you", attempts, "tries to guess rigth")
        break # Break loop
    computer_guess = 0 # Re-initialize computer_guess

# Check if limited_guess is equals to 0 and player_number not equals to computer_guess
if limited_guess == 0 and player_number != computer_guess:
    print("\nLol after", attempts, "tries you could not guess rigth")