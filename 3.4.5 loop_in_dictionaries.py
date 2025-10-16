"""
! Loop Dictionaries
! Loop Through a Dictionary
* You can loop through a dictionary by using a for loop.
* When looping through a dictionary, the return value are the keys of the dictionary, but
* there are methods to return the values as well.

? Example: Print all key names in the dictionary, one by one:
thisdict = {"fruit": "apple", "state": "kashmir"}
for x in thisdict:
    print(x)

? Output: fruit
          state

? Exmaple: Print all values in the dictionary, one by one:
thisdict = {"fruit": "apple", "state": "kashmir"}
for x in thisdict:
    print(thisdict[x])

? Output: apple
          kashmir

? Example: You can also use the values() method to return values of a dictionary:
thisdict = {"fruit": "apple", "state": "kashmir"}
for x in thisdict.values():
    print(x)

? Output: apple
          kashmir


? Example: You can use the keys() method to return the keys of a dictionary
thisdict = {"fruit": "apple", "state": "kashmir"}
for x in thisdict.keys():
    print(x)

? Output: fruit
          state


? Example: Loop through both keys and values, by using the items() method
thisdict = {"fruit": "apple", "state": "kashmir"}
for x, y in thisdict.items():
    print(x, y)

? Output: fruit apple
          state kashmir
"""
