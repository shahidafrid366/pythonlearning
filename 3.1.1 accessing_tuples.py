"""
! Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:

? Example: Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

? Output: banana


! Negative indexing
Negative indexing means start from the end.
-1 refers to the last item, -2 refers to the second last item etc

? Example: Print the last item of the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

? Output: 'cherry'


! Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

? Example: Return the third, fourth, and fifth item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

* Note: The search will start at index 2 (included) and end at index 5 (not included).
? Output: ('apple', 'banana', 'cherry')

* By leaving out the start value, the range will start at the first item:
? Example: This example returns the items from the beginning to, but NOT included, "kiwi"
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
? Output: ('apple', 'banana', 'cherry', 'orange')

* By leaving out the end value, the range will go on to the end of the tuple:
? Example: This example returns the items from "cherry" and to the end
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[4:])

? Output: ('kiwi', 'melon', 'mango')


! Range of Negative Indexes
* Specify negative indexes if you want to start the search from the end of the tuple:

? Example: This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

? Output: ('orange', 'kiwi', 'melon')


! Check if Item Exists
* To determine if a specified item is present in a tuple use the in keyword:

? Example: Check if "apple" is present in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

? Output: Yes, 'apple' is in the fruits tuple



"""
