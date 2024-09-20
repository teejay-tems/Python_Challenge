# Task: Grocery Store Receipt Generator
# Instructions:
    # 1. Write a Python program that simulates a simple grocery store receipt generator.
    # 2. Start by displaying a welcome message using a triple-quoted string (""" or '''). The
         # message should explain that the program will ask the user to input the names and prices
         # of items, and then generate a receipt at the end.
    # 3. Use escape sequences like \n for new lines and \t for indenting text to make the
        # message organized and easy to read.
# Your program should:
     # • Ask the user to input the names and prices of items.
     # • Calculate the total cost of all items.
     # • Display a neatly formatted receipt with item names, prices, and the total cost.

# Psuedo Code
# Display welcom message
# Initialize a variable string (item_one) and ask the user for input
# Initialize a variable integer (price_one) and ask the user for input
# Initialize a variable string (item_two) and ask the user for input
# Initialize a varaiable integer (price_two) and ask the user for input
# Initialize a variable string (item_three) and ask the user for input
# Initialize a variable integer (price_three) and ask the user for input

# Initialize a variable (total_cost) equals to (price_one) + (price_two) + (price_three)
# Display receipt


# Display message interpretation
print(
    """
       \t\t\t\tWelcome to Stephany supermarket:
       \n Please enter three product of your choice and their prices \
and I will issue you a recipt
    """
   )

# Get the user input
Name = input("Enter your name: ").title()
item_one = input("Enter your product: ").capitalize()
price_one = int(input("Enter product price: "))

item_two = input("Enter your product: ").capitalize()
price_two= int(input("Enter product price: "))

item_three = input("Enter your product: ").capitalize()
price_three = int(input("Enter product price: "))

#Calculate the total price
total_cost = price_one + price_two + price_three

# Receipt Summary
print(
     "\t\tStephany Receipt",
     "\n\t\t To",Name,
     "\n\t\t items\t price",
     "\n\t\t",item_one,"\t", price_one,
     "\n\t\t",item_two,"\t", price_two,
     "\n\t\t",item_three,"\t", price_three,
     "\n\t\t------ ------"
     "\n\t\t total", "\t", total_cost  
    )

