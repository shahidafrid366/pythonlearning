"""
! Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

* Use the copy() method
You can use the built-in List method copy() to copy a list.

? Example: Make a copy of a list with the copy() method:
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

    ? Output: ["apple", "banana", "cherry"]

! Use the list() method (built-in method)
Another way to make a copy is to use the built-in method list().

? Example: Make a copy of a list with the list() method:
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)

    ? Output: ["apple", "banana", "cherry"]


! Use the slice Operator
You can also make a copy of a list by using the : (Slice) operator.
The slice operator [:] is used to extract a portion of a sequence (like a list, string, or tuple) by specifying a start, stop, and step.

Basic Syntax: sequence[start:stop:step]

start: Index to begin slicing (inclusive)
stop: Index to end slicing (exclusive)
step: Interval between elements


lst = [0, 1, 2, 3, 4, 5]

lst[1:4]     # [1, 2, 3]
lst[:3]      # [0, 1, 2]
lst[::2]     # [0, 2, 4]
lst[::-1]    # [5, 4, 3, 2, 1, 0] (reverses the list)

Copying with Slice:
copy = lst[:]  # Creates a shallow copy of the list

This is useful to avoid modifying the original list when making changes to the copy.

Shallow Copy Note:
[:] copies the outer list.
Nested objects (like inner lists) are not deeply copied.
Use copy.deepcopy() for full duplication of nested structures.

Works with:
Lists
Strings
Tuples
Any sequence type

? Example: Make a copy of a list with the : operator:
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist[:]
    print(mylist)

    ? Output: ["apple", "banana", "cherry"]

"""
