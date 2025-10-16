## Basic Variable Naming Rules
# -----------------------------
"""
1. Start naming variables with letters or underscores (A-Z, a-z, _ )
age = 25                # Valid
_secret = "shahid"      # Valid
2fast = "Danger"        # Invalid / Error

2. Use letters, numbers or underscores (aa, a1, a_, a_b)
user_age_2 = 22              # Valid
best_friend_1 = "afrid"      # Valid
my-age = 23                  # Invalid

3. Variables are Case-sensitive
variables are case-sensitive For example. from below declarations you can see they serve the same
purpose, these are three distinct variables due to case sensitivity

age = 25
Age = 35
AGE = 45

4. You cannot use reserved words as variables Ex. print, if, else, from etc.
from = "shahid"     # invalid because from is a keyword and this throws error



Best Practices:
---------------
1. Be Descriptive: Your variable name should serve the purpose. Don't assign random names to them.
age = 25        # Valid
a = 25          # Acceptable, but it is difficult to identify its purpose

2. Use underscores for spaces
You can use Underscores (_) instead of spaces
first_name = "shahid"           # Valid
second name = "afrid"           # Invalid throws an error
firstname = "shahid"            # Valid but hard to read

3. Keep it simple: variable names should be short and sweet they shouldn't be so long
max_speed = 100                             # Valid
maximum_speed_on_highway_for_car = 150      # still valid but its very long


Common Mistakes
---------------
1. Don't use numbers before the variable. Ex:
1st_name = "shahid"

2. Using spaces between variables
first name = "afrid"

3. Using special characters
user@email = "shahid_123@gmail.com

"""


# Task 1: Variable Declarations
# Declare variables of different types (string, integer, float, boolean)
first_name = "John"
sport = "Baseball"
num1 = 5
num2 = 8.4
is_python_fun = True
string_number = "9"

# Task 2: Printing Variables
# Print each variable declared above
# Hint: Use the print() function
print(first_name)
print(sport)
print(num1)
print(num2)
print(is_python_fun)
print(string_number)

# Task 3: Operations with Variables
# Create a new variable 'result' and assign it the sum of num1 and num2
# Print the result
result = num1 + num2
print(result)

# Task 4: Modifying Variables
# Increment 'result' by 1
# Multiply 'result' by num1
# Print the new value of 'result'
result += 1
print(result)
result *= num1
print(result)

# Task 5: Creating a New Variable
# Create a new string variable 'second_name' with the value "Sam"
# Print the value of 'second_name'
second_name = "Sam"
print(second_name)

# Task 6: Whitespace Example
# Create a new string variable 'full_name' with a space between first and last name
# Print 'full_name'
full_name = "John Smith"
print(full_name)


# Example for printing 3 decimals only
ab = 10
abc = 34.342356
abcd = ab + abc
print(f"{abcd:.3f}")    # Output: 44.342

# When you divide 4/2 in python it gives output: 2.0 instead of 2 because python treats this as floating values
# when you use like this 4//2 it gives output: 2 so this extra care is required when working with integers

