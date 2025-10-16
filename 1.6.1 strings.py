"""
! Strings
Strings are sequences of characters enclosed in double quotes or in single quotes.

len() determines the length of string

indexing allows to access individual characters
indexing starts with 0 or either -1 both are supported
Negative indices represent the last character from the string & positive indicates first character of string


! Slicing:
Extracting the substring from a string
Syntax:- string[start:end:step]
    start - start of the substring
    end - end of the substring
    step - the step at which the substring starts [default is]


! Concatenation & Repetition:
Concatenation - joining the strings with + operator
Repetition  - repeating the strings with * operator
string methods for manipulation
Case change: upper(), lower()
Character replacement: replace()


"""

# ! ---  Indexing Examples  ---
greeting = "Hello, World"
name = "shahid_afrid"

print(greeting[0:5])  # Output: Hello
print(greeting[1:5])  # Output: ello
print(
    greeting[-1:5]
)  # Output: <blank line> because python slicing works only from left to right
print(
    greeting[-1:-5]
)  # Output: <blank line> because start index is -1 (-d) & end index is -5 (W).
# Since no step is provided, it defaults to +1, i.e., left to right

#! Important Rule: If start index is after end index (when using positive step), the result is an empty string.
print(
    greeting[-1:-5:-3]
)  # Output: do - because indexing starts from -1 so it prints d, index ends
# at -5(W) W won't be printed, -3 this is step it tells that it has to
# move three steps from current positing and print that letter so d is printed
print(
    greeting[1:5:3]
)  # Output: eo - because for positive indexing, index starts from 0 so eo is printed
print(greeting[-1])  # Output: d
print(
    greeting[::2]
)  # Output: hlo ol - since there is no start and end index so it will print
# all the letters from that variable with 2 step
print(greeting[::-2])  # Output: drW,le - this will print from last character

print(name[0:5])  # Output: shahi
print(name[1:5])  # Output: hahi
print(
    name[-1:5]
)  # Output: <blank line> because python slicing works only from left to right
print(
    name[-1:-5]
)  # Output: <blank line> because start index is -1 (-d) & end index is -5 (a).
# Since no step is provided, it defaults to +1, i.e., left to right
print(
    name[-1:-5:-3]
)  # Output: df because indexing starts from -1 so it prints d, index ends
# at -5(a) W won't be printed, -3 this is step it tells that it has to
# move three steps from current positing and print that letter so f is printed
print(
    name[1:5:3]
)  # Output: hi : because for positive indexing, index starts from 0 so hi is printed
print(name[-1])  # Output: d
print(name[::2])  # Output: sai_fi
print(name[::-2])  # Output: dradhh


# ! ---  Concatenation & Repetition Examples ---
greeting = "Hello, World"
name = "shahid_afrid"

print(greeting + "Python")  # Output: Hello, WorldPython

message = greeting + " " + "Python"
print(message)  # Output: Hello World Python


message = greeting, "Python"
print(message)  # Output: ("Hello, World", "Python")
# Here you're using a comma (,) between two items,
# which does not concatenate them as strings. Instead, the comma creates
# a tuple, a data structure in Python that holds multiple items.
# Tuples are used to group values together, but they don’t combine them into a single string.
# The comma creates a tuple of two elements:
# The first element: "Hello, World"
# The second element: "Python" So Output is: ("Hello, World", "Python)

# ! --- Repetition with *  ---
name_repeat = name * 3
print(name_repeat)  # Output: shahid_afridshahid_afridshahid_afrid

# Using string methods
name = "shahid_afrid"

print(name.lower())  # Output: shahid_afrid
print(name.upper())  # Output: SHAHID_AFRID
print(name.title())  # Output: Shahid_Afrid
print(name.capitalize())  # Output: Shahid_afrid - First letter is capital
print(
    name.replace("d", "dd")
)  # Output: shahid_afridd it will replace new characters with old one's

print(name.center(17, "*"))  # Output: ***shahid_afrid**
# center() this method is used to center the content
# the value you are passing should be greater than the string character.
# You can pass any padding characters like *, -, =, /, _, &, ^, %, #,@ etc

print(
    name.casefold()
)  # convert a string to lowercase, but with a stronger emphasis on case
# normalization than lower(). It's especially useful for case-insensitive
# string comparisons, particularly when dealing with text in different
# languages that might have special cases or accented characters

## Coding Exercise
# Task 1: Create string variables
greeting = "Hello, World!"
name = "Alice"

# Task 2: Print the length of the greeting string
# Your code here
print(len(greeting))

# Task 3: Use indexing to print specific characters
# Your code here
print(greeting[0])
print(greeting[2])
print(name[-1])

# Task 4: Use slicing to print parts of strings
# Your code here
print(greeting[:5])
print(name[2:4:1])

# Task 5: Print the greeting string in reverse
# Your code here
print(greeting[::-1])

# Task 6: Perform string concatenation
# Create full_name without a space and full_name_space with a space
# Your code here
full_name = name + "Wonderland"
print(full_name)
full_name_space = name + " " + "Wonderland"
print(full_name_space)

# Task 7: Use string repetition
# Your code here
repetition = name
repetition *= 3
print(repetition)

# Task 8: Use string methods
# Your code here
print(greeting.upper())
print(name.lower())
print(name.replace("l", "x"))


### --- Word Game --- ###
# 1. Get word from user
word = input("Enter a word: ")

# 2. Print the length of word
word_length = len(word)
print(f"The word '{word}' has {word_length} characters")


"""
! String Methods 
* Python has set of built-in methods that you can use on strings
* Note: All string methods returns new values. They do not change the original string.


! Method	        Description
* ----------        ------------
capitalize()	    Converts the first character to upper case
casefold()	        Converts string into lower case
center()	        Returns a centered string
count()	            Returns the number of times a specified value occurs in a string
encode()	        Returns an encoded version of the string
endswith()	        Returns true if the string ends with the specified value
expandtabs()	    Sets the tab size of the string
find()	            Searches the string for a specified value and returns the position of where it was found
format()	        Formats specified values in a string
format_map()	    Formats specified values from a dictionary in a string
index()	            Searches the string for a specified value and returns the position of where it was found
isalnum()	        Returns True if all characters in the string are alphanumeric
isalpha()	        Returns True if all characters in the string are in the alphabet
isascii()	        Returns True if all characters in the string are ascii characters
isdecimal()	        Returns True if all characters in the string are decimals
isdigit()	        Returns True if all characters in the string are digits
isidentifier()	    Returns True if the string is an identifier
islower()	        Returns True if all characters in the string are lower case
isnumeric()	        Returns True if all characters in the string are numeric
isprintable()	    Returns True if all characters in the string are printable
isspace()	        Returns True if all characters in the string are whitespaces
istitle()	        Returns True if the string follows the rules of a title
isupper()	        Returns True if all characters in the string are upper case
join()	            Converts the elements of an iterable into a string
ljust()	            Returns a left justified version of the string
lower()	            Converts a string into lower case
lstrip()	        Returns a left trim version of the string
maketrans()	        Returns a translation table to be used in translations
partition()	        Returns a tuple where the string is parted into three parts
replace()	        Returns a string where a specified value is replaced with a specified value
rfind()	            Searches the string for a specified value and returns the last position of where it was 
                    found
rindex()	        Searches the string for a specified value and returns the last position of where it was 
                    found
rjust()	            Returns a right justified version of the string
rpartition()	    Returns a tuple where the string is parted into three parts
rsplit()	        Splits the string at the specified separator, and returns a list
rstrip()	        Returns a right trim version of the string
split()	            Splits the string at the specified separator, and returns a list
splitlines()	    Splits the string at line breaks and returns a list
startswith()	    Returns true if the string starts with the specified value
strip()	            Returns a trimmed version of the string
swapcase()	        Swaps cases, lower case becomes upper case and vice versa
title()	            Converts the first character of each word to upper case
translate()	        Returns a translated string
upper()	            Converts a string into upper case
zfill()	            Fills the string with a specified number of 0 values at the beginning






"""
