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
Comparision operator always returns boolean values: True or False

We have 10 comparision operators in Python

<       : less than
<+      : less than or equal
>       : greater than
>=      : greater than or equal
==      : equal
!=      : not equal
is      : object identity
is not  : negated object identity
in      : membership
not in  : negated membership


4. Logical Operators
--------------------
and - Returns True if both operands are true
or - Returns True if at least one operand are true
not - Returns the opposite Boolean value


5. Identity Operators
---------------------
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
Below are the Identity Operators
is -> Returns True if both variables are the same object. Example: x is y
is not -> Returns True if both variables are not the same object. Example: x is not y

Example of is operator:
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   ## returns True because z is the same object as x

print(x is y)   # returns False because x is not the same object as y, even if they have the same content

print(x == y)   ## to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


Example of is not operator:
The is not operator returns True if both variables do not point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


Difference between is and ==
-----------------------------
is : checks if both variables point to same object in memory
== : checks if the values of both variables are equal

Example:
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)   # prints True since this compares the contents of variables
print(x is y)   # prints False since this checks the memory address of x & y variables
print(id(x))    # prints the unique memory address of x (2392424015552)
print(id(y))    # prints the unique memory address of y (2392424164160)



6. Membership Operator
-----------------------
Membership operators are used to test if a sequence is presented in an object.
in     - Returns True if a sequence with the specified value is present in the object. Ex: x in y
not in - Returns True if a sequence with the specified value is not present in the object. Ex: x not in y

Example for in:
Check if "banana" is present in a list:
fruits = ["apple", "banana", "orange"]
print("banana" in fruits)


Example for not in:
Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)


Membership in Strings
---------------------
The membership operators also work with strings
Example:
text = "Hello World"

print("H" in text)      # True
print("hello" in text)  # False
print("z" not in text)  # True



7. Bitwise Operator
-------------------
Bitwise operators are used to compare (binary) numbers

Operator	Name	                Description
& 	        AND	                    Sets each bit to 1 if both bits are 1   Example: x & y
|	        OR	                    Sets each bit to 1 if one of two bits is 1 Example: x | y
^	        XOR	                    Sets each bit to 1 if only one of two bits is 1 Example: x ^ y
~	        NOT	                    Inverts all the bits    Example: ~x
<<	        Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off    Example: x << 2
>>	        Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off Example: x >> 2


Example 1: The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110  The binary representation of 6 is 0110
# 3 = 0011  The binary representation of 3 is 0011
# --------
# 2 = 0010
print(6 & 3)    # Then the & operator compares the bits and returns 0010, which is 2 (0010) in decimal.


Example 2: The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
# 6 = 0110  # The binary representation of 6 is 0110
# 3 = 0011  # The binary representation of 3 is 0011
# --------
# 7 = 0111

print(6 | 3)    # Then the | operator compares the bits and returns 0111, which is 7 (0111) in decimal.


Example 3: The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0
# 6 = 0110  # The binary representation of 6 is 0110
# 3 = 0011  # The binary representation of 3 is 0011
# --------
# 5 = 0101  # Then the ^ operator compares the bits and returns 0101, which is 5 (0101) in decimal.


Example 4: The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).
print(~3)   # Output -4
Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100


Example 5: Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(3 << 2)   # 12

The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100


Example 6: Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

print(8 >> 2)   # Output: 2

The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100



8. Operator Precedence
----------------------
Operator precedence describes the order in which operations are performed

Example 1: Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first
print((6 + 3) - (6 + 3))    # Output: 0

Example 2: Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions
print(100 + 5 * 3)  # Output: 115


Precedence Order:
The precedence order is described in the table below, starting with the highest precedence at the top

Operator	            Description
()	                    Parentheses
**	                    Exponentiation
+x  -x  ~x	            Unary plus, unary minus, and bitwise NOT
*  /  //  %	            Multiplication, division, floor division, and modulus
+  -	                Addition and subtraction
<<  >>	                Bitwise left and right shifts
&	                    Bitwise AND
^	                    Bitwise XOR
|	                    Bitwise OR
==, !=, >, >=, <, <=    is  is not  in  not in 	Comparisons, identity, and membership operators
not	                    Logical NOT
and	                    AND
or	                    OR


Left to Right Evaluation
If two operators have the same precedence, the expression is evaluated from left to right.

Example: Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right
print(5 + 4 - 7 + 3)    # Output:5


"""

# Assignment Operators
# Simple Assignment
x = 10
print(x)

# Addition Assignment
x += 5
print("x += 5, ", x)

# Subtraction Assignment
x -= 2
print("x -= 3,", x)

# Multiply Assignment
x *= 2
print("x *= 2,", x)

# Division Assignment
x /= 2
print("x /= 2, ", x)


# Comparison Operator
print("5 == 5:", 5 == 5)  # True
print("5 == 6:", 5 == 6)  # False

print("5 != 5:", 5 != 5)  # False
print("5 != 6:", 5 != 6)  # True

print("5 > 5: ", 5 > 5)  # False
print("5 < 6: ", 5 < 6)  # True

print("5 >= 6: ", 5 >= 6)  # False
print("5 <= 6: ", 5 <= 6)  # True


# Logical Operator
print("True and True: ", True and True)  # True
print("True and False: ", True and False)  # False

print("True or True:", True or True)  # True
print("True or False:", True or False)  # True
print("False or True:", False or True)  # True
print("False or False:", False or False)  # False

print("not True:", not True)  # False
print("not False:", not False)  # True


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
else:
    result = "Enter Valid numbers"
print(result)


# Assignment Operators Example
# Simple Assignment
x = 10
print(x)

# Addition Assignment
x += 5
print("x += 5, ", x)

# Subtraction Assignment
x -= 2
print("x -= 3,", x)

# Multiply Assignment
x *= 2
print("x *= 2,", x)

# Division Assignment
x /= 2
print("x /= 2, ", x)


# Comparison Operator Examples
print("5 == 5:", 5 == 5)  # True
print("5 == 6:", 5 == 6)  # False

print("5 != 5:", 5 != 5)  # False
print("5 != 6:", 5 != 6)  # True

print("5 > 5: ", 5 > 5)  # False
print("5 < 6: ", 5 < 6)  # True

print("5 >= 6: ", 5 >= 6)  # False
print("5 <= 6: ", 5 <= 6)  # True


# Logical Operator Examples
print("True and True: ", True and True)  # True
print("True and False: ", True and False)  # False

print("True or True:", True or True)  # True
print("True or False:", True or False)  # True
print("False or True:", False or True)  # True
print("False or False:", False or False)  # False

print("not True:", not True)  # False
print("not False:", not False)  # True


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
else:
    result = "Enter Valid numbers"
print(result)


# Modulor Operator Examples
print(10 / 2)  # Division: Output 5.0
print(10 // 2)  # Division: Output 5

print(10 * 2)  # Multiplication: Output 20

print(10**2)  # Output: 100 base ** exponent operation like square, cube, etc


# Modulo operation
# dividend % divisor = Remainder
print(10 % 3)  # Output: 1
print(15 % 4)  # Output: 3

# Calculate 3 to the power of 4, and find the remainder when dividend by 5
# print(3 ** 4)             # 3 to power of 4 = 81
remainder = (3**4) % 5
print(remainder)  # Remainder = 1


# Calculate the volume of cube
# 1. Store the length of cube's side (let's say that its 4 units)
# 2. Calculate the volume using formula (volume = side length * side length)
# 3. print the results
side_length = 4
volume = side_length**3
print(f"Volume of cube = {volume}")
