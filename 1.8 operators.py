"""
In Python, we have different types of operators

1. Arithmatic Operators
-----------------------
Addition Operators (+)
Subtraction Operators (-)
Multiplication Operators (*)
Division Operators (/)
Floor Division Operators (//)   - Divides and rounds down to nearest integer
Modulo Operators (%)            - Returns the remainder of the division
Exponentiation Operators (**)   - Raises the left operand to the power of right operand


2. Assignment Operators
-----------------------
Simple assignment (=)
Addition Operators (+=)     - Adds the right operand & assigns to left operand & assigns result to left operand
Subtraction Operators (-=)  - Subtracts the right operand & assigns to left operand & assigns result to left operand
Multiplication Operator (*=) - Multiplies the right operand & assigns to left operand & assigns result to left operand
Division Operator (/=)       - Divides the right operand & assigns to left operand & assigns result to left operand


3. Comparison Operators
------------------------
equal to (==)   - checks if two values are equal
not equal to (!=) - checks if two values are not equal
greater than (>) - checks if two values are greater than
less than (<) - checks if two values are less than
greater than or equal to (>=) - checks if two values are greater than or equal to or equal
less than or equal to (<=) - checks if two values are less than or equal to or equal


4. Logical Operator
-------------------
and - Returns True if both operands are true
or - Returns True if at least one operand are true
not - Returns the opposite Boolean value

"""

# Assignment Operators
# Simple Assignment
x = 10
print(x)

# Addition Assignment
x += 5
print("x += 5, ",x)

# Subtraction Assignment
x -= 2
print("x -= 3,", x)

# Multiply Assignment
x *= 2
print("x *= 2,", x)

# Division Assignment
x /= 2
print("x /= 2, ",x)


# Comparison Operator
print("5 == 5:",5==5)       # True
print("5 == 6:",5==6)       # False

print("5 != 5:",5!=5)       # False
print("5 != 6:",5!=6)       # True

print("5 > 5: ",5>5)        # False
print("5 < 6: ",5<6)        # True

print("5 >= 6: ",5>=6)      # False
print("5 <= 6: ",5<=6)      # True


# Logical Operator
print("True and True: ", True and True)         # True
print("True and False: ", True and False)       # False

print("True or True:", True or True)            # True
print("True or False:", True or False)          # True
print("False or True:", False or True)          # True
print("False or False:", False or False)        # False

print("not True:", not True)                    # False
print("not False:", not False)                  # True


# Simple Calculator
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print(num1 + num2)
if num1.isnumeric() and num2.isnumeric():
    result = int(num1) + int(num2)
elif num1.isdecimal() and num2.isdecimal():
    result = float(num1) + float(num2)
elif num1.isdigit() and num2.isdecimal():
    result = int(num1) + float(num2)
elif num1.isdecimal() and num2.isdigit():
    result = float(num1) + int(num2)
else :
    result = "Enter Valid numbers"
print(result)
