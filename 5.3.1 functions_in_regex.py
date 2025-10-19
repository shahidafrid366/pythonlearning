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

import re

text = "Hello world, Say Hello to Python"
pattern = r"Hello"
another_pattern = r"Python"

search = re.search(pattern, text)
another_search = re.search(another_pattern, text)

if search:
    print(
        "Match found:", search.group(), search.span()
    )  # Output: Match found: Hello (0, 5) # This returns first match where it finds and ignores the second Hello word
else:
    print("No Match found")

if another_search:
    print("Match found:", another_search.group(), another_search.span())
else:
    print("Mathc Not found")



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


! re.finditer()
* Returns match objects — useful when you need details like position.

import re

text = "There is rain in India"
pattern = r"in"

matches = re.finditer(pattern, text)

for m in matches:
    print(
        f"Match: {m.group()} at position {"Start Position:", m.start(), "End Position:",m.end(), m.span()}"
    )   # India is ignore in the output since i is capital here


! re.findall()
* Returns all matches at a list.
import re

text = "The rain in India stays mainly in the plain"
pattern = r"in"

matches = re.findall(pattern, text)
print(matches)  # India is ignore in the output since i is capital here



! re.split()
* Splits a string by regex pattern

import re

text = "apple:banana;orange|kiwi.grapes-strawberry'tomato"
pattern = r"[.,;|:'-]"

result = re.split(pattern, text)
print(result)

# Output: ['apple', 'banana', 'orange', 'kiwi', 'grapes', 'strawberry', 'tomato']
# In character class ([]) whatever the characters you mention it will split the strings based on that character class
# You can even add numbers in or letters in the character class and use them for splitting
# In below example lets add one more item using ^ and will see the output for it

import re

text1 = "apple:banana;orange|kiwi.grapes-strawberry'tomato^pineapple"
pattern1 = r"[.,;|:'-]"

result = re.split(pattern1, text1)
print(result)

# Output: ['apple', 'banana', 'orange', 'kiwi', 'grapes', 'strawberry', 'tomato^pineapple']



! re.sub()
Replaces the text matching pattern

import re

text = "Welcome to Mumbai"
pattern = r"mumbai"

sub = re.sub(pattern, "india", text, flags=re.IGNORECASE)
print(sub)

# Output: Welcome to andra pradesh



! re.compile()
Used for efficiency — compile a pattern once, then reuse it.



"""

import re

text = "Welcome to Mumbai"
pattern = r"mumbai"

sub = re.sub(pattern, "andra pradesh", text, flags=re.IGNORECASE)
print(sub)
