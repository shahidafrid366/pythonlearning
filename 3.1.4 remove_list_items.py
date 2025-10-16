"""
! Remove Specified Item
The remove() method removes the specified item.

? Example: Remove banana
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)

    ? Output: ['apple', 'cherry']

If there are more than one item with the specified value, the remove() method removes
the first occurrence:
? Example: In this list we have two banana items
    thislist = ["apple", "banana", "cherry", "banana"]
    thislist.remove("banana")
    print(thislist)

    ? Output: ['apple', 'cherry', 'banana']
    ? This will only remove the first occurence and keeps the rest


! Remove specified Index
The pop() method removes the specified index.

? Example: Remove the second item:
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)

    ? Output: ['apple', 'cherry']

    * If you do not specify the index, the pop() method removes the last item.
    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)

    ? Output: ['apple', 'banana']

    * The del keyword also removes the specified index:
    ? Example:
        thislist = ["apple", "banana", "cherry"]
        del thislist[0]
        print(thislist)

    ? Output: ['banana', 'cherry']

    * The del keyword can also delete the entire list completely
    ? Example: Delete the entire list
        thislist = ["apple", "banana", "cherry"]
        del thislist


! Clear the List
The clear() method empties the list.
The list still remains, but it has no content.

? Example: Clear the list content:
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)

    ? Output: []
"""
