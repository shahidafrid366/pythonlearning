"""
! Access Items
* You cannot access items in a set by referring to an index or a key.
* But you can loop through the set items using a for loop, or ask if a specified value is present in a set,
* by using the in keyword.

? Example 1: Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

? Output:    apple
             banana
             cherry

? Example 2: Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

? Output: True

? Example 3: Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

? Output: False


! Change Items
* Once a set is created, you cannot change its items, but you can add new items.
"""
