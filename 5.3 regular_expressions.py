"""
! RegEx
* A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
* RegEx can be used to check if a string contains the specified search pattern.


! Example usage of RegEx
- Used in form validations to validate the mobile no's, email id's & etc.
- Used in pattern matching applications like: Functionality of ctrl+f and Replace, grep commands in linux, LIKE operator in SQL
- To create translators in compilers, interpreters, assemblers for syntax analysis & lexical analysis
- Syntax analysis like validating the syntaxes of programs
- Lexical analysis like validating the keywords (operators, variables, etc) & normal text. This seperates them
- Data Extractions: you can extract the specific information from the data like extracting dates from the text
- Data cleaning & Data formatting: You can remove extra whitespaces or unwanted characters from given data
- Web Scraping: regex can be used to locate and extract specific content or information from HTML or XML documents. Ex: You want to extract the URL's from webpage
- Password Policies: Use in NLP to validate the length of passwords & specific patterns


! RegEx Module
* Python has a built-in package called re, which can be used to work with Regular Expressions.
* Import the re module:
? import re


! Basic Search Functions
There are number of functions in Search Functions in python. They are dependent on ways of working
* re.search()
* re.match()
* re.finditer()
* re.findall()
* re.split()
* re.sub()
* re.compile()
* etc.


! 1. re.search()
* Syntax: re.search(pattern, data)
*   pattern: The regular expression pattern you want to search for.
*   data: data/input string in which you want to search for pattern
* Returns: match object if match if found, or None if match is not found.

? Example: Searching for matching patterns
import re
pattern = "python"
data = "python is very powerful, python has lots of features"

match = re.search(pattern, data)
print(match)
print(type(match))
? Output: <re.Match object; span=(0, 6), match='python'>
          <class 're.Match'>

? Example: Searching for not matching patterns
import re
pattern = "xyz"
data = "python is very powerful, python has lots of features"

match = re.search(pattern, data)
print(match)
print(type(match))
? Output: None
          <class 'NoneType'>

? Example: For the above example we will be using more meaningful output statements
import re
pattern = "python"
data = "python is very powerful, python has lots of features"

match = re.search(pattern, data)
print(match)
print(type(match))

if match:
    print("found")
else:
    print("Not found")
? Output: <re.Match object; span=(0, 6), match='python'>
          <class 're.Match'>
          found

? Example: If you want to include which word is found you can do it by using group() method
import re
pattern = "python"
data = "python is very powerful, python has lots of features"

match = re.search(pattern, data)
print(match)
print(type(match))

if match:
    print("found: ", match.group())
else:
    print("Not found")
? Output: <re.Match object; span=(0, 6), match='python'>
          <class 're.Match'>
          found python

! Flags: We have couple of flags in searching module in python. Flags are Optional
* re.A (Flag) | re.A (Long Syntax) - Perform ASCII-only matching instead of full Unicode matching
* re.I (Flag) | re.IGNORECASE (Long Syntax) - Perform case-insensitive matching
* re.M (Flag) | re.MULTILINE (Long Syntax) - This flag is used with metacharacter ^ (caret) and $ (dollar). When this flag is specified, the metacharacter ^ matches the pattern at beginning of the string and each newline’s beginning (\n). And the metacharacter $ matches pattern at the end of the string and the end of each new line (\n)
* re.S (Flag) | re.DOTALL (Long Syntax) - Make the DOT (.) special character match any character at all, including a newline. Without this flag, DOT(.) will match anything except a newline
* re.X (Flag) |	re.VERBOSE (Long Syntax) - Allow comment in the regex. This flag is useful to make regex more readable by allowing comments in the regex.
* re.L (Flag) | re.LOCALE (Long Syntax) - Perform case-insensitive matching dependent on the current locale. Use only with bytes patterns

? Example: Using IGNORECASE flag
import re

pattern = "PYTHON"
data = "python is very powerful, it has lots of features"

match = re.search(pattern, data, re.IGNORECASE)
print(match)
print(type(match))

if match:
    print("found: ", match.group())
else:
    print("Not found")
? Output: <re.Match object; span=(0, 6), match='python'>
          <class 're.Match'>
          found:  python



! 2. re.Match()
* Purpose: search for a pattern at the beginning of a string
* Syntax: re.match(pattern, data, flag=0)    #Flags are optional
    pattern = The regular expression you are searching for
    data = The input string/the data you are passing to search for.
* Returns: If a match is found at the beginning of string, it returns a match object, otherwise it return None

? Example: search for python at beginning of a line
? Using raw string for ignoring escape sequence
import re

word_to_search = "python"
input_string = "Python is very powerful, it has lots of features"

searching_for_match = re.match(word_to_search, input_string, re.I)
print(searching_for_match)
print(type(searching_for_match))

if searching_for_match:
    print("found: ", searching_for_match.group())
else:
    print("Not found")
? Output: <re.Match object; span=(0, 6), match='python'>
          <class 're.Match'>
          found:  Python


? Example: Change in input string
? Using raw string for ignoring escape sequence
import re

word_to_search = r"python"
input_string = "The Python is very powerful, it has lots of features"

searching_for_match = re.match(word_to_search, input_string, re.I)
print(searching_for_match)
print(type(searching_for_match))

if searching_for_match:
    print("found: ", searching_for_match.group())
else:
    print("Not found")
? Output: None
          <class 'NoneType'>
          Not found


! You can use regular expressions in two ways:
    * 1. directly [patterns(as strings)]  - direct way of using like above
    * 2. regular expressions objects - there are lots of advantages one of it is performance enhancement

! 2. regular expressions objects
* Syntax: re.compile(pattern, flags)    # flags are optional
? Example:
import re

pattern = re.compile(r"PYthon", re.IGNORECASE)
data = "python is powerful language"

match = re.match(pattern, data)
print(match)
print(type(match))
if match:
    print("found:", match.group())
else:
    print("Not found")

? Output: <re.Match object; span=(0, 6), match='python'>
          <class 're.Match'>
          found: python

! RegEx in Python
* When you have imported the re module, you can start using regular expressions

? Example: Search the string to see if it starts with "India" and ends with "countries"
import re

txt = "India is among the greatest countries"
x = re.search("^India.*countries$", txt)
if x:
    print("Matched")
else:
    print("No Match")
? Output: Matched
* Search pattern is case sensitive. It searches as it is. See below example

import re

txt = "India is among the greatest countries"
x = re.search("^india.*countries$", txt)    # replacing I with i and it gives No Match
if x:
    print("Matched")
else:
    print("No Match")
? Output: No Match


! RegEx Functions
* The re module offers a set of functions that allows us to search a string for a match:

*Function	Description
*--------   -----------
findall	    Returns a list containing all matches
search	    Returns a Match object if there is a match anywhere in the string
split	    Returns a list where the string has been split at each match
sub	        Replaces one or many matches with a string

"""

import re

pattern = re.compile(r"PYthon", re.IGNORECASE)
data = "python is powerful language"

match = re.match(pattern, data)
print(match)
# print(type(match))
if match:
    print("found:", match.group())
else:
    print("Not found")
