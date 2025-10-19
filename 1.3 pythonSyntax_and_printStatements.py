# Python Syntax
# Python syntax can be executed by writing directly in the Command Line
# >>> print("Hello, World!")
# Hello, World!

# Or by creating a python file on the server, using the .py file extension, and running it in the Command Line:
# python myfile.py


# Python Indentation
# Indentation refers to the spaces at the beginning of a code line.
# Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
# Python uses indentation to indicate a block of code.

# Example:
if 5 > 2:
    print("Five is greater than two")

# Python will give you an error if you skip the indentation
# Example:
# if 5 > 2:
# print("Five is greater than two")
# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.

# The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one
# if 5 > 2:
#  print("Five is greater than two!")
# if 5 > 2:
#         print("Five is greater than two!")

# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error


## Print Statements
print("Hello World in with basic structure")

print("Print Statement with single quotes")  # Print statement with single quotes
print("Print Statement with double quotes")  # Print statement with double quotes

# Semicolons (Optional, Rarely Used)
# Semicolons are optional in Python. You can write multiple statements on one line by separating them with ;
# but this is rarely used because it makes it hard to read:
# Example:
print("Hello")
print("How are you?")
print("Bye bye!")

# However, if you put two statements on the same line without a separator (newline or ;),
# Python will give an error:
# print("Python is fun!") print("Really!")      # Error: invalid syntax

# Best practice: Put each statement on its own line so your code is easy to understand.


# Printing using \n
print(
    "Hello World \n" "New line\n" "Another line"
)  # This will print two statements in two different lines


# Printing statements using "" & '' inside the print
print("Using 'Single quotes' in print statement")
print('Using "Double quotes" in print statement')


# By using \n in the print statement you can print the string in different lines
print("Example of using \n with print statement:")
print("Shahid\nAfrid")


# By using just \t it will print tab spaces
print(
    "Here we are using 'slash t' between words so it prints tab spaces:- Shahid\tAfrid"
)


# Using Comma in print statements to print spaces
print("Example Using commas", "My name is", "Shahid", "I am", 30, "years old")


# Using \ & \\
print("It's awesome\\")


# Printing the text in new lines
# Generally your will use to print text in new lines like this
print("First line")
print("Second line")

# Instead of using multiple print statements like above we can use special escape characters
# This is one way of printing but this is a bit clumsy
print("First Line\nSecond line\nThird line")

# You can use this method for maintaining hygiene coding
print(
    """First line,
Second line,
Third line."""
)

print(
    """First line,
Second line,
Third line"""
)

## Printing blank lines between lines
# This is traditional method of doing
print("First line")
print()
print("Second line")

# But use this to use single print statement
print("First line \n\nSecond line\n\nThird line")

# You can also use this method for maintaining hygiene
print(
    """First line

second line"""
)


## Escape characters
print(
    """Escape Characters:
\\n - Starts a new line
\\t - Adds tab spaces
\\ - Prints a backslash
\\ - Prints a backslash
\" - Adds double quotes
\' = Adds single quotes"""
)
