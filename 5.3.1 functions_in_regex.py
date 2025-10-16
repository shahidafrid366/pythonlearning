"""
! Functions in Regex
* There are lot many functions in Regex. Some of them are used most widely and some of them are used rarely

? Important ones are:
* re.search()   - Searches anywhere in the string for the first match
* re.match()    - Checks for a match only at the beginning of a string
* re.finditer() - Returns an iterator of match objects (for detailed info)
* re.findall()  - Returns all matches as a list
* re.split()    - Splits a string using regex patterns
* re.sub()      - Replaces parts of a string using a regex
* re.compile()  - Compiles a regex pattern for repeated use (performance boost)


! re.search()
* Searches anywhere in the string and returns the first match.




! re.match()
* Searches only at the beginning of the string.

import re  # Imports regex module

text = "Hello World"
pattern = r"Hello"

match = re.match(pattern, text)  # re.match() looks for the first occurrence of pattern anywhere in the string. If it finds it returns match object, if not it returns None
if match:
    print("Word Matched:", match.group())  # match.group() returns the exact substring that matched your pattern.
else:
    print("Word Not Matched")

? Output: Match found: Hello


! re.search()
* Searches anywhere in the string and returns the first match.


"""

import re

text = "Hello world, Say Hello to Python"
pattern = r"Hello"
another_pattern = r"Python"

search = re.search(pattern, text)
another_search = re.search(another_pattern, text)

if search:
    print(
        "Match found:", search.group(), search.span()
    )  # Output: Match found: Hello (0, 5) # This returns first match where it founds
else:
    print("No Match found")

if another_search:
    print("Match found:", another_search.group(), another_search.span())
else:
    print("Mathc Not found")
