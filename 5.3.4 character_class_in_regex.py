"""
! Character Classes in Python
* A character class in regex defines a set or range of characters that you want to match.
* They are written inside square brackets [ ] and match any single character from that set.

* You can use a dash - to specify a range
* Use a caret ^ inside the brackets to match characters not in the set.

? Example 1:
import re
pattern = r"[abc]"
data = "apple"
match = re.findall(pattern, data)
print(match)

? Output: ['a']
? Explanation: [abc] means match either 'a', 'b', 'c'. In 'apple', only 'a' matches


? Example 2:
import re

pattern = r"[0-9]"
data = "The price IS $100"

match_list = re.finditer(pattern, data)
for match in match_list:
    print(match)
? Output: <re.Match object; span=(14, 15), match='1'>
          <re.Match object; span=(15, 16), match='0'>
          <re.Match object; span=(16, 17), match='0'>


? Example: Find and print if digits are present in the data
import re

data = "total number of students are 100"
pattern = r"[0-9]"

match_list = re.finditer(pattern, data)
print(match_list)
if match_list:
    print("Digits Available")
else:
    print("Digits Not Available")
? Output: ['1', '0', '0'] Digits Available
* You can remove digits and check the output




! Character Classes
-------------------
* [abc]: Matches any one of the characters 'a', 'b', or 'c'.
* [^abc]: Matches any character that is not 'a', 'b', or 'c'.
* [0-9]: Matches any digit from '0' to '9'.
* [A-Z]: Matches any uppercase letter from 'A' to 'Z'.
* [a-z]: Matches any lowercase letter from 'a' to 'z'.
* [A-Za-z]: Matches any uppercase or lowercase letter.
* [0-9A-Fa-f]: Matches a hexadecimal digit (0-9, A-F, or a-f).
* [a-zA-Z0-9]: Matches any alphanumeric character.
* [^0-9]: Matches any character that is not a digit.
* [^A-Za-z]: Matches any character that is not an uppercase or lowercase letter.






"""

import re

data = "total number of students are 100"
pattern = r"[0-9]"

match_list = re.finditer(pattern, data)
print(match_list)
if match_list:
    print("Digits Available")
else:
    print("Digits Not Available")

#
import re

data = "total number of students are 100"
pattern = r"[0-9]"

match_list = re.finditer(pattern, data)
print(match_list)
if match_list:
    print("Digits Available")
else:
    print("Digits Not Available")
