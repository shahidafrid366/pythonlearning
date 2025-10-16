"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

? Syntax: lambda arguments : expression
* The expression is executed and the result is returned:

? Example: Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))

? Output: 15


* Lambda functions can take any number of arguments:
? Example: Multiply argument a with argument b and return the result
x = lambda a, b: a * b
print(x(5, 6))
? Output: 30

x = lambda a, b: a * b
print(x(5, 2.4))
? Output: 12

? Example: Summarize argument a, b, and c and return the result
x = lambda a, b, c : a + b + c
print(x(1, 2, 3))
? Output: 6




!! Why Use Lambda Functions?
* The power of lambda is better shown when you use them as an anonymous function inside another function.
* Say you have a function definition that takes one argument, and that argument will be multiplied with an
* unknown number:
? Example:
def myfunc(n):
  return lambda a : a * n


* Use that function definition to make a function that always doubles the number you send in:
? Example:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))

? Output: 22


* Or, use the same function definition to make a function that always triples the number you send in:

? Example:
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))

? Output: 33

* Or, use the same function definition to make both functions, in the same program:

Example
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

? Output: 22
          33

* Use lambda functions when an anonymous function is required for a short period of time.
"""

# 1. Square a number using lambda
square = lambda n: n * n
print(square(2))

# 2. Add two numbers
addition = lambda a, b: a + b
print(addition(2, 2))

# 3. Get the last character of a string
last_character = lambda word: word[-1]
# print(last_character(input(f"Enter the string to print last character: ")))

# 4. Check if a number is even
# Use a lambda to check if a number is even (returns True or False).
# number = int(input(f"Enter the number: "))  # Asks the number from user and converts it to integer
is_even = (
    lambda x: x % 2 == 0
)  # here x holds the value entered by user for ex: 4 and this line becomes 4%2=0
# print(is_even(number))  # This line calls lambda function using the number entered by user & prints result.


# 5. Sort a list of tuples by the second element
# Given: pairs = [(1, 3), (2, 1), (4, 2)]
# Sort it using sorted() and a lambda as the key.

pairs = [(1, 3), (2, 1), (4, 2)]

# Sort by the second element of each tuple
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)


# 7. Filter out odd numbers
# Use filter() and a lambda to keep only even numbers from:
# nums = [1, 2, 3, 4, 5, 6]
nums = [1, 2, 3, 4, 5, 6]
""" nums is the variable that holds the list of numbers 
# you’re telling Python: “Apply this lambda function to every element inside the list stored in nums.” """
odd_nums = list(filter(lambda num: num % 2 != 0, nums))
print(odd_nums)


# 8. Map names to uppercase
# Use map() and a lambda to convert a list of names to uppercase:
# names = ['alice', 'bob', 'charlie']
names = ["alice", "bob", "charlie"]
uppercase = list(map(lambda name: name.upper(), names))
print(uppercase)


# 9. Sort strings by their length
# Sort a list like this:
# words = ['apple', 'banana', 'kiwi', 'cherry']
words = ["apple", "banana", "kiwi", "cherry"]
word = list(len((lambda str: str, words)))
print(word)


# Create a lambda that returns the max of two numbers
# Example: max_lambda(10, 20) should return 20.

# Use lambda inside reduce to multiply all elements
# Given:
# from functools import reduce
# nums = [2, 3, 4]
# Multiply all elements using reduce() and a lambda.
