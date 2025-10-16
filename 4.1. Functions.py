""" "
! Definition:
* A function is a block of reusable code that performs a specific task.
* Instead of writing the same logic multiple times, you can define it once inside a function -
* and call it whenever you need.

! 1. Defining a function
* You define a function using the "def" keyword

def greet():
    print("Hello! Welcome to Python functions.")

* Here:
    def - Keyword to define function
    greet - Function name
    () - parenthesis (can hold parameters)
    : - indicates start of function block
    code inside function must be indented


! 2. Calling a function
* You can (call) the function by writing its name with parenthesis:

? Example: greet()
* Output: Hello! Welcome to Python functions.


! 3. Functions with Parameters (inputs)
* You can pass values to a function:

def greet(name):
    print(f"Hello {name}, welcome to python"):

call it like:
greet("Shahid")

? Example:
def greet(name):
    print(f"Hello {name}, welcome to python")

greet(input("Enter your name:"))


! Functions with multiple parameters
def add(num1, num2):
    print("sum -", num1 + num2)

add(5,4)

Output: sum - 9


! Returning Values
* Functions can return results using the return statement:

def add(a,b):
    return a + b

result = add(5,4)
print("Result: ",result)

? Output: Result: 30


! 6. Default Parameter
* If no value is passed, the default is used:

def greeting(name="Shahid"):
    print(f"Hello {name}")

greeting()              # Used default value.  Output: Hello Shahid
greeting('Afrid')       # Uses given value.    Output: Hello Afrid

* [If we don't pass any value with function it will take default value]



! 7. Keyword Arguments
* You can pass arguments by name:

def introduce(name, age):
    print(f"Hello {name}, your age is {age}")

introduce(age=23, name="shahid")


! 8. Variable Number of Arguments
* Sometimes you don't know how many values will be passed.

*args → multiple positional arguments (tuple)
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4, 5))

? Output: 21


**kwargs → multiple keyword arguments (dictionary)
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="shahid", age=34, country="India")

? Output:
name = Shahid
age = 25
country = India


! 9. Nested Functions
* A function inside another function:

def outer(name="Shahid"):
    print(f"outer function {name}")
    def inner(age=34):
        print(f"inner function {age}")
        print(f"outer function {name}")
    inner()
outer()


! 10. Lambda Functions (Anonymous Functions)
* Small, one-line functions without def:

square = lambda x: x * x
print(square(5))

? Output: 25


! Python Built-in Functions
* Function	        Description
abs()	            Returns the absolute value of a number
all()	            Returns True if all items in an iterable object are true
any()	            Returns True if any item in an iterable object is true
ascii()	            Returns a readable version of an object. Replaces none-ascii characters with escape character
bin()	            Returns the binary version of a number
bool()	            Returns the boolean value of the specified object
bytearray()	        Returns an array of bytes
bytes()	            Returns a bytes object
callable()	        Returns True if the specified object is callable, otherwise False
chr()	            Returns a character from the specified Unicode code.
classmethod()	    Converts a method into a class method
compile()	        Returns the specified source as an object, ready to be executed
complex()	        Returns a complex number
delattr()	        Deletes the specified attribute (property or method) from the specified object
dict()	            Returns a dictionary (Array)
dir()	            Returns a list of the specified object's properties and methods
divmod()	        Returns the quotient and the remainder when argument1 is divided by argument2
enumerate()	        Takes a collection (e.g. a tuple) and returns it as an enumerate object
eval()	            Evaluates and executes an expression
exec()	            Executes the specified code (or object)
filter()	        Use a filter function to exclude items in an iterable object
float()	            Returns a floating point number
format()	        Formats a specified value
frozenset()     	Returns a frozenset object
getattr()	        Returns the value of the specified attribute (property or method)
globals()	        Returns the current global symbol table as a dictionary
hasattr()	        Returns True if the specified object has the specified attribute (property/method)
hash()	            Returns the hash value of a specified object
help()	            Executes the built-in help system
hex()	            Converts a number into a hexadecimal value
id()	            Returns the id of an object
input()	            Allowing user input
int()	            Returns an integer number
isinstance()	    Returns True if a specified object is an instance of a specified object
issubclass()	    Returns True if a specified class is a subclass of a specified object
iter()	            Returns an iterator object
len()	            Returns the length of an object
list()	            Returns a list
locals()	        Returns an updated dictionary of the current local symbol table
map()	            Returns the specified iterator with the specified function applied to each item
max()	            Returns the largest item in an iterable
memoryview()	    Returns a memory view object
min()	            Returns the smallest item in an iterable
next()	            Returns the next item in an iterable
object()	        Returns a new object
oct()	            Converts a number into an octal
open()	            Opens a file and returns a file object
ord()	            Convert an integer representing the Unicode of the specified character
pow()	            Returns the value of x to the power of y
print()	            Prints to the standard output device
property()	        Gets, sets, deletes a property
range()	            Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
repr()	            Returns a readable version of an object
reversed()	        Returns a reversed iterator
round()	            Rounds a numbers
set()	            Returns a new set object
setattr()	        Sets an attribute (property/method) of an object
slice()	            Returns a slice object
sorted()	        Returns a sorted list
staticmethod()	    Converts a method into a static method
str()	            Returns a string object
sum()	            Sums the items of an iterator
super()	            Returns an object that represents the parent class
tuple()	            Returns a tuple
type()	            Returns the type of an object
vars()	            Returns the __dict__ property of an object
zip()	            Returns an iterator, from two or more iterators

"""


## Practical Examples:
# 1. Write a function say_hello() that prints "Hello, Python!"
def say_hello():
    print("Hello, Python!")


say_hello()


# 2. Write a function greet(name) that takes a name as input and prints "Hello <name>"
def greet(name):
    print(f"Hello {name}")


greet("Shahid")


# 3. Write a function square(num) that returns the square of a number.
def square(num):
    return num * num


result = square(100)
print("Square of 100: ", result)


# 4. Write a function even_or_odd(num) that prints whether the number is even or odd.
def even_or_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


even_or_odd(12)


# 🔹 Level 2: Functions with Multiple Parameters
# 5. Write a function add(a, b) that returns the sum of two numbers.
def add(a, b):
    return a + b


result = add(1, 2)
print(result)


# 6. Write a function area_of_rectangle(length, width) that returns the area.
def area_of_rectangle(length, width):
    return length * width


result = area_of_rectangle(100, 10)
print(f"Area Of Rectangle: {result}")


# 7. Write a function is_divisible(a, b) that returns True if a is divisible by b, else False.
def is_divisible(a, b):
    return a % b == 0


result = is_divisible(2, 2)
print(result)


# 8. Write a function max_of_three(a, b, c) that returns the largest number.
def max_of_three(a, b, c):
    return max(a, b, c)


result = max_of_three(2, 3, 4)
print(result)


# 🔹 Level 3: Default & Keyword Arguments
# 9. Write a function greet(name="Guest") that prints "Hello, <name>".
def greet(name="Guest"):
    print(f"Hello {name}")


greet()


# 10. Write a function power(num, exp=2) that returns num raised to the power exp.
def power(num, exp=2):
    return num**exp


result = power(6)
print(result)


# 11. Write a function introduce(name, age, city="Unknown") and test it using keyword arguments.
def introduce(name, age, city="Unknown"):
    print(f"Hello {name}, your age is {age}, city is {city}")


introduce(name="Shahid", age=23)


# 🔹 Level 4: Variable Arguments
# 12. Write a function sum_all(*args) that returns the sum of any number of numbers.
def sum_all(*args):
    return sum(args)


result = sum_all(34, 5353, 234, 34)
print(result)


# 13. Write a function show_info(**kwargs) that prints all key-value pairs.
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


show_info(name="shahid", age=23, address="hyd")


# 14. Write a function multiply_all(*args) that returns the product of all numbers.
def multiply_all(*args):
    product = 1
    for num in args:
        product *= num
    return product


result = multiply_all(2, 3, 4, 5, 6, 7, 8, 9)
print(result)


# 🔹 Level 5: Return & Logic
# Write a function factorial(n) that returns factorial using a loop.
def factorial(n):
    factorial = 1
    for f in range(1, n + 1):
        factorial = factorial * f
    return factorial


result = factorial(4)
print(result)

# Write a function is_prime(n) that returns True if n is prime, else False.
# def is_prime(n):


# Write a function fibonacci(n) that prints the first n Fibonacci numbers.


# 🔹 Level 6: Advanced
# Write a function palindrome(word) that checks if a string is a palindrome.
#
# Write a function count_vowels(s) that counts how many vowels are in a string.
#
# Write a lambda function to find the cube of a number.
#
# Write a lambda function to filter even numbers from a list.
