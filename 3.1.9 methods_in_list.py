"""
! List Methods
* Python has a set of built-in methods that you can use on lists.

Method	    Description
---------   -----------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list


"""

# append()
fruits1 = ["apple", "banana"]
fruits1.append("orange")
print(fruits1)

a = ["apple", "banana"]
b = ["BMW", "Ford"]
a.append(b)
print(a)
b.append(a)
print(b)

# clear()
fruits2 = ["apple", "banana"]
fruits2.clear()
print(fruits2)

# copy()
fruits3 = ["apple", "banana"]
fruits4 = fruits3.copy()
fruits3.append("guava")

print(fruits3)
print(fruits4, id(fruits3), id(fruits4))


# count()
numbers = [1, 2, 3, 5, 3, 2, 5, 3, 4, 1]
count = numbers.count(3)
print(count)


# extend()
fruits5 = ["apple", "banana"]
fruits5.extend(["orange"])
print(fruits5)

fruits5.append(["ornage, banana"])
print(fruits5)

# append() v/s extend()
# append():
# Purpose: Adds a single element to the end of the list.
# Syntax: list.append(element)
# Behavior: The entire element is added as one item, even if it's a list.

fruits6 = ["apple", "banana"]
fruits6.append("cherry")
print(fruits6)  # ['apple', 'banana', 'cherry']

fruits6.append(["mango", "orange"])
print(fruits6)  # ['apple', 'banana', 'cherry', ['mango', 'orange']]

# * Notice how the inner list is added as a single item.

# extend():
# Purpose: Adds each element of an iterable (like a list, tuple, or string) to the list.
# Syntax: list.extend(iterable)
# Behavior: The elements of the iterable are added individually

# Example:
fruits = ["apple", "banana"]
fruits.extend(["mango", "orange"])
print(fruits)  # ['apple', 'banana', 'mango', 'orange']

# Here, "mango" and "orange" are added as separate items.


# index()
# The index() method returns the position at the first occurrence of the specified value.
# Syntax: list.index(element, start, end)
# Parameter values:
# element: Required. Any type (string, number, list, etc.). The element to search for
# start:   Optional. A number representing where to start the search
# end:     Optional. A number representing where to end the search

# Example1: What is the position of the value 32
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)  # Output: 5

# Example2: Find the postion of 'cherry', but start the search at position 4
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "cherry"]
x = fruits.index("cherry", 4)
print(x)  # Output: 6


# insert()
# The insert() method inserts the specified value at the specified position.
# Syntax: list.insert(position, element)

# Example:
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']


# pop()
# The pop() method removes the element at the specified position.
# Syntax: list.pop(position)
# default value is -1, which returns the last item
# Note: The pop() method returns removed value.

# Example:
fruits = ["apple", "banana", "cherry"]
fruits.pop(1)
x = fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry']
print(x)  # Output: banana    # Returns the removed item.


# sort()
# The sort() method sorts the list ascending by default.
# You can also make a function to decide the sorting criteria(s).

# Syntax: list.sort(reverse=True|False, key=myFunc)
# Parameters
# reverse:	Optional. reverse=True will sort the list descending. Default is reverse=False
# key:   	Optional. A function to specify the sorting criteria(s)

# Example:
cars = ["Ford", "BMW", "Volvo"]
print(cars.sort())  # Output: ['BMW', 'Ford', 'Volvo]
print(cars.sort(reverse=True))  # Output: ['Volvo', 'Ford', 'BMW']


# Example: Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)


cars = ["Ford", "Mitsubishi", "BMW", "VW"]
cars.sort(key=myFunc)  # Output: ['VW', 'BMW', 'Ford', 'Mitsubishi']


# Example: Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
    return e["year"]


cars = [
    {"cars": "BMW", "year": 1998},
    {"cars": "Volvo", "year": 2000},
    {"cars": "Bugati", "year": 1995},
]
cars.sort(key=myFunc)
print(cars)

cars.sort(reverse=True, key=myFunc)
print(cars)
