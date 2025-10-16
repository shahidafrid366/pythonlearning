print("Hello World in with basic structure")

print('Print Statement with single quotes')  # Print statement with single quotes
print("Print Statement with double quotes")  # Print statement with double quotes

print("Hello World \n"
      "New line\n""Another line")   # This will print two statements in two different lines

print("Using 'Single quotes' in print statement")
print('Using "Double quotes" in print statement')

# By using \n in the print statement you can print the string in different lines
print("Example of using '\n' with print statement:")
print("Shahid\nAfrid")

# By using just \t it will print tab spaces
print("Here we are using 'slash t' between words so it prints tab spaces:- Shahid\tAfrid")

# Using Comma in print statements to print spaces
print("Example Using commas","My name is","Shahid","I am",30,"years old")

# Using \ & \\
print('It\'s awesome\\')

#################################
#################################

# Printing the text in new lines

# Generally your will use to print text in new lines like this
print("First line")
print("Second line")

# Instead of using multiple print statements like above we can use special escape characters

# This is one way of printing but this is a bit clumsy
print("First Line\nSecond line\nThird line")

# You can use this method for maintaining hygiene coding
print("""First line,
Second line,
Third line.""")

print('''First line,
Second line,
Third line''')

## Printing blank lines between lines
# This is traditional method of doing
print("First line")
print()
print("Second line")

# But use this to use single print statement
print("First line \n\nSecond line\n\nThird line")

# You can also use this method for maintaining hygiene
print("""First line

second line""")


## Escape characters
print("""Escape Characters:
\\n - Starts a new line
\\t - Adds tab spaces
\\ - Prints a backslash
\\ - Prints a backslash
\" - Adds double quotes
\' = Adds single quotes""")