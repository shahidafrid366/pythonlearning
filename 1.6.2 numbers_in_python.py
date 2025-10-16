"""
! Python Numbers

There are three numeric types in Python:
    int
    float
    complex
Variables of numeric types are created when you assign a value to them:
? Example:
    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex


* To verify the type of any object in Python, use the type() function:
? Example:
    print(type(x))
    print(type(y))
    print(type(z))


! int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

? Example: Integers
    x = 1
    y = 35656222554887711
    z = -3255522

    print(type(x))
    print(type(y))
    print(type(z))


! Float
* Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

? Example: Float
    x = 1.10
    print(type(x))

    ? Output:  <class 'float'>

* Float can also be scientific numbers with an "e" to indicate the power of 10.
? Example: Floats
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

? Output: <class 'float'>
          <class 'float'>
          <class 'float'>


! Complex
* Complex numbers are written with a "j" as the imaginary part:
? Example:  x = 3+5j
            y = 5j
            z = -5j

            print(type(x))
            print(type(y))
            print(type(z))
    ? Output: <class 'complex'>
              <class 'complex'>
              <class 'complex'>


! Type Conversion
* You can convert from one type to another with the int(), float(), and complex() methods:

? Example: Convert from one type to another
#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)        # 1.0
print(y)        # 2
print(z)        # (1+0j)

print(type(x))  # <class 'float'>
print(type(y))  # <class 'int'>
print(type(z))  # <class 'complex'>

* Note: You cannot convert complex numbers into another number type


! Random Number
* Python does not have a random() function to make a random number, but Python has a
* built-in module called random that can be used to make random numbers:

? Example: Import the random module, and display a random number from 1 to 9:
import random
print(random.randrange(1, 10))

? Output: 5  # This will generate random output like 5 or 2 or 3 or 7

* In our Random Module Reference you will learn more about the Random module.


"""
