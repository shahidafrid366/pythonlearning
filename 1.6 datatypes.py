"""
! Basic Built-in Data Types
int     : Integer numbers (e.g., 5, -3, 100)
float   : Floating-point numbers (e.g., 3.14, -0.001)
complex : Complex numbers (e.g., 2 + 3j)
bool    : Boolean values (True, False)
str     : String/text data (e.g., "Hello", 'Python')


! Sequence Types
* Used to store ordered collections:
list    : Mutable sequence (e.g., [1, 2, 3])
tuple   : Immutable sequence (e.g., (1, 2, 3))
range   : Sequence of numbers (e.g., range(0, 10))


! Text Type
str     : Already mentioned above, used for text.


! Set Types
* Used for unordered collections of unique elements:
set         : Mutable set (e.g., {1, 2, 3})
frozenset   : Immutable set


! Mapping Type
* Used for key:value pairs:
dict        : Dictionary (e.g., {"name": "Shaik", "role": "Contractor"})


! Binary Types
* Used for binary data:
bytes       : Immutable binary data
bytearray   : Mutable binary data
memoryview  : Memory view object


! None Type
NoneType    : Represents the absence of a value (None)


! Custom/User:defined Types
* You can define your own types using:
Classes     : via class keyword
Enums       : via enum.Enum


! Setting the Data Type
* In Python, the data type is set when you assign a value to a variable:


! Example	                                    Data Type
* -------                                       ---------
x = "Hello World"	                            str
x = 20	                                        int
x = 20.5	                                    float
x = 1j	                                        complex
x = ["apple", "banana", "cherry"]	            list
x = ("apple", "banana", "cherry")	            tuple
x = range(6)	                                range
x = {"name" : "John", "age" : 36}	            dict
x = {"apple", "banana", "cherry"}	            set
x = frozenset({"apple", "banana", "cherry"})	frozenset
x = True	                                    bool
x = b"Hello"	                                bytes
x = bytearray(5)	                            bytearray
x = memoryview(bytes(5))	                    memoryview
x = None	                                    NoneType


"""

from traceback import print_list

## We will see few data types assignment
age = 30
name = "Shahid"
pi = 3.14
is_new = True

# With type function we can check the data types. Example
# type()
print("Prints type of age variable", type(age))
print("Prints type of name variable", type(name))
print("Prints type of pi variable", type(pi))
print("Prints type of is_new variable", type(is_new))

print("Name is:", name)
print("Age is", age)
print("pi value is:", pi)
print("is student", is_new)


## Determining the data types of following values
# In Python, you can directly know the type of the value like below
5
3.14
"Shahid"
True
-7
"88"
False
0.0
print(type(5))
print(type(3.14))
print(type("Shahid"))
print(type(True))
print(type(-7))
print(type(False))
print(type(0.0))

## Variable Assignment Manipulation

# 1. Create a variable named 'age' and assign it your age as integer
age = 27

# 2. Create a variable called 'height' and assign it your height in meters as a float
height = 2.26

# 3. Create a variable called 'name' and assign it your name as a string
name = "Shahid"

# 4. Create a variable called 'is_student' and assign it a boolean value indicating whether you're a student
is_student = False

# 5. Print out all the variables
print(age)
print(height)
print(name)
print(is_student)

# 6. Increase the age variable by 1 and print it out
# print(age+1)
age += 1  # += is shortcut for addition and re-assignment
print(age)

# 7. Multiply the height variable by 100 to convert it to centimeters and print it out
# print(height * 100)
height *= 100
print(height)

# 8. Add "is my name" to the 'name' variable and print it out
# print(f"{name} is my name")
name += " is my name "  # += is shortcut for addition and re-assignment
print(name)

# 9. Change 'is_student' to opposite and print it out
print(not is_student)
