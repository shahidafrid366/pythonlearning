# Addition of Numbers by taking input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

sum_of_numbers = num1 + num2 + num3

print(f"Sum of Total Numbers = {sum_of_numbers}")


# Let's see basic example of input
name = input("Enter your name: ")
print(name)

age = input("Enter your age: ")
print(age)

# **Important: Python will always consider the input as a string even if it is integer.
# Ex: If user enters 18 it will consider as string "18" but not as integer 18.
print(
    type(age)
)  # If you observe this you will understand that python considers this as string

# We have to explicitly convert age string to age integer
convert_age_as_string_to_integer = int(age)  # converting string to integer
print(type(convert_age_as_string_to_integer))

# 1. Greeting Program
# Create a simple program to aks user's name to greet them with personalized greeting

name = input("May i know your name? ")
message = input("Enter your greeting message: ")
print(f"Hello {name}, {message}")


# 2. Echo Machine Program
# Create a simple program that will prompt the user to type something and then repeat it back exactly
# same as entered

age = input("Enter your age: ")
print(f"Your entered age is: '{age}'")


# 3. Favorite Colour
# Write a program that inquired about user's favorite colour and responds with the comment
# about that colour
color = input("Enter your favorite color: ")
print(f"{color}, it reminds me of plants which produces oxygen")


# Multiple Inputs Exercises
# 4. Create a program that gathers user's name, age, hometown and then crafts a summary sentence
# using this information

name = input("Enter your name: ")
age = input("Enter your age: ")
hometown = input("Enter your hometown: ")

print(f"Hello '{name}', you are '{age}' years old. Your Address is: {hometown}")


# Converting inputs to their appropriate datatypes
# 5. Create a program that asks for user's name and convert it into integer then calculate and print
# their age in 'dogs year' (multiply by 7)
humans_age = int(input("Enter your age: "))
dogs_age = humans_age * 7
print(f"You are {dogs_age:.2f} years old in dog years!")


# Simple Calculator
# 6. Calculate two numbers and perform arithmatic operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "invalid operation"
print(result)


# 7. Days to Hours
# Develop a program that asks for number of days, convert it into integer and then calculate and print
# equivalent number into hours
days = int(input("Enter number of days: "))
hours = 24 * days
print(f"{days} days has {hours} hours.")


from datetime import datetime  # Using libraries

birth_year = input("Enter Your Birth Year: ")
# current_year = input("Enter Current Year: ")
current_year = datetime.now().year

birth_year = int(birth_year)
current_year = int(current_year)

age = current_year - birth_year
print(f"You're '{age}' years old")

# 1. Greeting Program
# Create a simple program to aks user's name to greet them with personalized greeting

name = input("May i know your name? ")
message = input("Enter your greeting message: ")
print(f"Hello {name}, {message}")


# 2. Echo Machine Program
# Create a simple program that will prompt the user to type something and then repeat it back exactly
# same as entered

age = input("Enter your age: ")
print(f"Your entered age is: '{age}'")


# 3. Favorite Colour
# Write a program that inquired about user's favorite colour and responds with the comment
# about that colour
color = input("Enter your favorite color: ")
print(f"{color}, it reminds me of plants which produces oxygen")


# Multiple Inputs Exercises
# 4. Create a program that gathers user's name, age, hometown and then crafts a summary sentence
# using this information

name = input("Enter your name: ")
age = input("Enter your age: ")
hometown = input("Enter your hometown: ")

print(f"Hello '{name}', you are '{age}' years old. Your Address is: {hometown}")


# Converting inputs to their appropriate datatypes
# 5. Create a program that asks for user's name and convert it into integer then calculate and print
# their age in 'dogs year' (multiply by 7)
humans_age = int(input("Enter your age: "))
dogs_age = humans_age * 7
print(f"You are {dogs_age:.2f} years old in dog years!")


# Simple Calculator
# 6. Calculate two numbers and perform arithmatic operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "invalid operation"
print(result)


# 7. Days to Hours
# Develop a program that asks for number of days, convert it into integer and then calculate and print
# equivalent number into hours
days = int(input("Enter number of days: "))
hours = 24 * days
print(f"{days} days has {hours} hours.")
