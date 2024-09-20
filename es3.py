# Write a program that simulates a fortune cookie. The program
# should display one of five unique fortunes, at random, each
# time it’s run.
import random
# fortune_cookie = random.randint(1,5)
# print(fortune_cookie)

# name = ["paul","peter","samuel","chima"]
# print(name[0])
# print(name.index("paul"))

# for i in name:
#     print(i)

# number = [10,20,30,50,70]
# for k in number:
#     if k > 100:
#         print("high value")
#     elif k < 11:
#         z = k
#         k=k+1
#         print("low number",number.index(z))
#         break
#     else:
#         print("poor value")

# exam = "pass"

# while exam == "pass":
#     print("fail")
#     break

# 4. Task
# Here’s a bigger challenge. Write the pseudocode for a program
# where the player and the computer trade places in the number
# guessing game. That is, the player picks a random number
# between 1 and 100 that the computer has to guess. Before you
# start, think about how you guess. If all goes well, try coding the
# game.

               # Pseudeocode

# set the initial values
# initialize a variable integer(number) randint (1,100) using random 
# initialize a variable integer(guess) using input to ask player to take a guess

# guessing the loop
# write a while loop statement if the guess != number
# set condition using if statement
# if guess < 100 print ("lower number")
# else: print ("higher number")
# Use the input variable (guess) to ask player to take another guess

# congratulating the player
# write a print statement to print("congratulation you guess it! The number is", number)
# write a print statement to exit the looop print("\n\n press the enter key to exit")


            # Interpretation
#set the initial values
number = random.randint(1,100)
guess = int(input("Take a guess: "))


# guessing the loop
while guess != number:
    if guess < 100:
        print("Lower number")
    else :
        print("Higher number")
    guess = int(input("Take a guess: "))
       
# congratulating the player
    print("\n\tYou guessed it!. The number is", number)

# exit the game
    input("\n\nPress the enter key to exit")




# 2. Task
# Write a program that flips a coin 100 times and then tells you
# the number of heads and tails.