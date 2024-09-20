# Task
# Modify the Guess My Number game so that the player has a
# limited number of guesses. If the player fails to guess in time,
# the program should display an appropriately chastising
# message.


            # Psudeocode
# Initialize a varable integer (limited_guess) equals to 3
# Initialize a variable (player_guess) equals to 0
# Intialize a variable (number) get random number from 1 to 100
# Initialize a variable (attempts) equals to None

# While (limited_guess) greater than 0

    # While (player_guess) not in range(1, 101)
        # Get (player_guess) from the player

    # (limited_guess) -= 1
    # (attempts) += 1

    # If (number) is greater than (player_guess)
        # Display guess higher
    # If (number) is less than (player_guess)
        # Display guess lower
    # If (number) equals (player_guess)
        # Display you are right
        # Display congratulation it took you (attempts) tries to guess right
        # Break
    # (player_guess) equals to 0

# If limited_guess is equals to 0 and player_guess is not equals tonumber:
    # Dispaly lol after (attempts) tries you could not guess the right number human





                # Implementation
# Initializations
import random
limited_guess = 3
player_guess = 0
number = random.randint(1, 100)
attempts = 0



while limited_guess > 0: # If limited guess is still greater than 0

    while player_guess not in range(1, 101): # Validate player input
        player_guess = int(input("\nPlease enter your guess (1, 100): "))

    limited_guess -= 1
    print("\nlimited_guess is: ", limited_guess)
    attempts += 1
    print("attempts is: ", attempts)
    print("computer number is: ", number)

    if number > player_guess:
        print("guess higher")
    elif number < player_guess:
        print("guess lower")
    else:
        print("you are correct")
        print("congratulation it took you", attempts, "tries to guess right")
        break
    player_guess = 0 # Re-initialize player_guess

if limited_guess == 0 and player_guess != number:
    print("lol after", attempts, "tries you could not guess the right number human")


    