"""
! 1. Introduction to Lists
Definition: A list is an ordered, mutable (changeable), collection that can hold different
data types

-> Lists are used to store multiple items in a single variable.
-> Lists are one of 4 built-in data types in Python used to store collections of data,
   the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

* Syntax: my_list = []

Examples: fruits = ["apple", "banana", "cherry"]  # List with values
          mixed = [10, "hello", 3.14, True]

? List
-> List items are ordered, changeable, and allow duplicate values.
-> List items are indexed, the first item has index [0], the second item has index [1] etc.

? Order
-> When we say that lists are ordered, it means that the items have a defined order,
   and that order will not change.
-> If you add new items to a list, the new items will be placed at the end of the list.

! Note: There are some list methods [append(), clear(), insert(), remove() etc.]
! that will change the order, but in general: the order of the items will not change.

? Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after
it has been created.

? Allow Duplicates
Since lists are indexed, lists can have items with the same value:

* Example: mylist = ["apple", "orange", "grapes", "apple"]

? List Length
To determine how many items a list has, use len() function
* Example: thislist = ["apple", "banana", "cherry"]
* print(len(thislist))

? List items - Data Types
List items can be of any type
* Example: string, int, boolean etc
* list1 = ["apple", "banana"]
* list2 = [1, 2, 3, 4]
* list3 = [True, False]

A list can contain different data types:
* list4 = ["apple", 3, 4.8, True]


? type()
From Python's perspective, lists are defined as objects with the data type 'list':
* <class 'list'>


? List Constructor list():
It is also possible to use the list() constructor when creating a new list.

* Example: thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
*          print(thislist)


"""
