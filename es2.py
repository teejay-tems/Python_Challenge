# Task : Create a Basic Calculator Program
# Instructions:
      # 1. Write a Python program that functions like a basic calculator.
      # 2. Use a triple-quoted string (""" or ''') for displaying messages.
      # 3. Incorporate escape sequences like \n for new lines and \t for tabs to make your output
        # organized and well-formatted.
# Your program should:
  # • Welcome the user.
  # • Ask the user to input two numbers.
  # • Perform and display the results of the following operations:
       # o Addition
       # o Subtraction
       # o Multiplication
       # o Division

# Psuedo Code
# Display welcome message 
# Initialize a variable integer (number_one) and ask the user for input 
# Initialize a variable integer (number_two) and ask the user for input 
# Initialize a variable (Addition) equals to (number_one) + (number_two)
# Initialize a variable (Subtraction) equals to (number_one) - (number_two)
# Initialize a variable (Multiplication) equals to (number_one) * (number_two)
# Initialize a variable (Division) equals to (number_one) / (number_two)
# Display (Addition),(Subtraction),(Multiplication),(Division)

#Interpretation
print(
    """
      \t\t\t\t Welcome to CalculateWithStephany program 
      \n\tThis program will ask the user to input two numbers and perform basic arithmethic operations intended like:
      \n\t\t- Addition
      \n\t\t- Subtraction
      \n\t\t- Multiplication
      \n\t\t- Division
    """
)

# Get user inputs
number_one = int(input("\nEnter your first number: ")) 
number_two = int(input("\nEnter your second number: ")) 

# Perform basic arithmetic operation
Addition = number_one + number_two
Subtraction = number_one - number_two
Multiplication = number_one * number_two
Division = number_one // number_two

# Display result
print(
    "\t\tResults: "
    "\n\t\t-Addition: ", Addition,
    "\n\t\t-Substraction: ", Subtraction,
    "\n\t\t-Multiplication: ",Multiplication,
    "\n\t\t-Division: ", Division
)


 