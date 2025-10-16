"""
! Add List Items

! Append Items
To add an item to the end of the list, use the append() method:
? Example: Using the append() method to append an item:
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)


! Insert Items
To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index:

? Example: Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

    ? Output: ['apple', 'orange', 'banana', 'cherry']
    ? Here orange is added in the second position
    ? Note: As a result of the examples above, the lists will now contain 4 items.


! Extend List
To append elements from another list to the current list, use the extend() method.

? Example: Add the elements of tropical to thislist:
    thislist = ["apple", "banana", "cherry"]
    tropical = ["mango", "pineapple", "papaya"]
    thislist.extend(tropical)
    print(thislist)

    ? Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
    ? The elements will be added to the end of the list.


! Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

? Exmaple: Add elements of a tuple to list
    thislist = ["apple", "banana", "cherry"]
    thistuple = ("kiwi", "orange")
    thislist.extend(thistuple)
    print(thislist)

    ? Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']
"""
