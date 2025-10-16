"""
* F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
* Before Python 3.6 we had to use the format() method.


! F-Strings
* F-string allows you to format selected parts of a string.
* To specify a string as an f-string, simply put an f in front of the string literal, like this

? Example: Create a f-string
txt = f"This is 49 dollars"
print(txt)

? Output: The price is 49 dollars


! Placeholders and Modifiers
* To format values in an f-string, add placeholders {}, a placeholder can contain variables, operations,
* functions, and modifiers to format the value.

? Example: Add a placeholder for the price variable
price = 100
txt = f"Total Bill is Rs.{price}"
print(txt)

* A placeholder can also include a modifier to format the value.
* A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed * point number with 2 decimals
? Example: Display the price with 2 decimals
price = 59.21345673254
txt = f"The price is {price:.4f} dollars"
print(txt)

? Output: The price is 59.2134 dollars


* You can also format a value directly without keeping it in a variable:
? Example: Display the value 95 with 2 decimals
txt = f"Price is {95.2345:.2f}"
print(txt)

? Output: Price is 95.23


!! Perform Operations in F-Strings
* You can perform Python operations inside the placeholders.
* You can do math operations:

? Example: Perform a math operation in the placeholder, and return the result
txt = f"Addition: {2+4}"
print(txt)

? Output: Addition: 6

* You can perform math operations on variables aswell
? Example:
a = 2
b = 4
txt = f"Addition: {a+b}"
print(txt)

? Output: Addition: 6


* You can perform if...else statements inside the placeholders:

? Example: Return "Expensive" if the price is over 50, otherwise return "Cheap"
a = 1
txt = f"{'a is greater' if a>5 else 'lesser'}  "
print(txt)

? Output: a is greater


! Execute Functions in F-strings
* You can execute functions inside the placeholder

? Example: Use the string method upper() to convert a value into upper case letters
fruit = "apple"
txt = f"converted {fruit} to caps {fruit.upper()}"
print(txt)


* The function does not have to be a built-in Python method, you can create your own functions and use them
? Example: Create a function that converts feet into meters
def converter(x):
    return x * 0.3048

txt = f"Plane is flying at {converter(10000)} meter altitude"
print(txt)

? Output: Plane is flying at 3048.0 meter altitude


! More Modifiers
* Earlier we understood how to use the .2f modifier to format a number into a fixed point number with 2
* decimals.

* There are several other modifiers that can be used to format values:

? Example: Use a comma as a thousand separator:
price = 10000000
txt = f"price is {price:,}"
print(txt)

? Output: price is 10,000,000


! Here is a list of all the formatting types.
* Formatting Types
:<		Left aligns the result (within the available space)
txt = f"I have {100:<10} rupees"
print(txt)
? Output: I have 100        rupees


:>		Right aligns the result (within the available space)
txt = f"I have {100:>10} rupees"
print(txt)
? Output: I have        100 rupees


:^		Center aligns the result (within the available space)
txt = f"price is {100:<10} rupees"
print(txt)
? Output: I have     100    rupees


:=		Places the sign to the left most position
* #Use "=" to place the plus/minus sign at the left most position:
txt = f"I have {+100 := 10} rupees"
print(txt)
? Output: I have        100 rupees


:+		Use a plus sign to indicate if the result is positive or negative
* Use "+" to always indicate if the number is positive or negative:
txt = f"The temperature is between {-3:+} and {7:+} degrees celsius."
print(txt)
? Output: The temperature is between -3 and +7 degrees celsius.


:-		Use a minus sign for negative values only
* Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = f"The temperature is between {-3:-} and {7:-} degrees celsius."
print(txt)
? Output: The temperature is between -3 and 7 degrees celsius.


: 		Use a space to insert an extra space before positive numbers (and minus sign before negative numbers)
* Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = f"The temperature is between {-3: }and{7: } degrees celsius."
print(txt)
? Output: The temperature is between -3and 7 degrees celsius. #(observe the spaces b/w -3, and, 7)


:,		Use a comma as a thousand separator
txt = f"I have {100000000:,} rupees."
print(txt)
? Output: I have 100,000,000 rupees.

:_		Use a underscore as a thousand separator
txt = f"The universe is {13800000000:_} years old."
print(txt)
? Output: The universe is 13_800_000_000 years old.


:b		Binary format
txt = f"I have {500:b} rupees."
print(txt)
? Output: I have 111110100 rupees.


:c		Converts the value into the corresponding Unicode character
txt = f"I have {50000:c} rupees."
print(txt)
? Output: I have 썐 rupees.


:d		Decimal format
* Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = f"I have {0b101:d} rupees."
print(txt)
? Output: I have 5 rupees.


:e		Scientific format, with a lower case e
* Use "e" to convert a number into scientific number format (with a lower-case e):
txt = f"We have {5:e} chickens."
print(txt)
? Output: We have 5.000000e+00 chickens.


:E		Scientific format, with an upper case E
* Use "E" to convert a number into scientific number format (with an upper-case E):
txt = f"We have {5:E} chickens."
print(txt)
? Output: We have 5.000000E+00.


:f		Fix point number format
* Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:
txt = f"The price is {45:.2f} dollars."
print(txt)
? Output: The price is 45.00 dollars.

* without the ".2" inside the placeholder, this number will be displayed like this:
txt = f"The price is {45:f} dollars."
print(txt)
? Output: The price is 45.000000 dollars.


:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
* Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:
x = float('inf')
txt = f"The price is {x:F} dollars."
print(txt)
? Output: The price is INF dollars.

* same example, but with a lower case f:
txt = f"The price is {x:f} dollars."
print(txt)
? Output: The price is inf dollars.


:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format


!! String format()
* Before Python 3.6 we used the format() method to format strings.
* The format() method can still be used, but f-strings are faster and the preferred way to format strings.
* The next examples in this page demonstrates how to format strings with the format() method.
* The format() method also uses curly brackets as placeholders {}, but the syntax is slightly different:

? Example: Add a placeholder where you want to display the price
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
? Output: The price is 49 dollars

* You can add parameters inside the curly brackets to specify how to convert the value:
? Example: Format the price to be displayed as a number with two decimals:
price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))
? Output: The price is 49.00 dollars


! Multiple Values
* If you want to use more values, just add more values to the format() method:
print(txt.format(price, itemno, count))

* And add more placeholders
? Example:
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
? Output: I want 3 pieces of item number 567 for 49.00 dollars.
* # Above order should match according to your requirement. it will print as it is


! Index Numbers
* You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:
? Example:
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
? Output: I want 3 pieces of item number 567 for 49.00 dollars.

* Also, if you want to refer to the same value more than once, use the index number:
? Example:
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
? Output: His name is John. John is 36 years old.


! Names Indexes
* You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
? Example:
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

? Output: I have a Ford, it is a Mustang.

"""
