"""
! Access Items
List items are indexed and you can access them by referring to the index number:
* Note: The first item has index 0.

? Example:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])  # in square bracket we have 1 so it prints the 1 indexed item

! Negative index
Negative indexing means start from the end
-1 refers to last item. -2 refers to second last item & etc

? Example:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])     # Prints cherry


! Range of indexes
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

? Example 1:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

Output: ['cherry', 'orange', 'kiwi']
*This will return the items from position 2 to 5.
*Remember that the first item is position 0,
*and note that the item in position 5 is NOT included

? Example 2:
* If you don't mention the range value it prints all the values from start value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

? Example 3:
* If you don't mention start value it prints all the values till range value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

Output: ['apple', 'banana', 'cherry', 'orange']


! Range of Negative Indexes
Specify negative indexes if you want to start the search from the end of the list:

? Example:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

* Negative indexing means starting from the end of the list.
* This example returns the items from index -4 (included) to index -1 (excluded)
* Remember that the last item has the index -1,


! Check if Item Exists
To determine if a specified item is present in a list use the in keyword:

? Example:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



"""
