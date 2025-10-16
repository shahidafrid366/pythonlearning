"""
! Once a set is created, you cannot change its items, but you can add new items.

! Add Items
* To add one item to a set use the add() method.
? Example: To add one item to a set use the add() method.
thisset = {"apple", "mango", "banana"}
thisset.add("orange")
print(thisset)

? Output: {'apple', 'mango', 'orange', 'banana'}


! Add Sets
* To add items from another set into the current set, use the update() method.

? Example 1: Add elements from newset into thisset:
thisset = {"apple", "banana"}
newset = {"orange"}
thisset.update(newset)
print(thisset)

? Output: {"apple", "banana", "orange"}


? Example 2: Add elements from three sets
* We can do this on two ways
thisset = {"apple", "banana"}
newset = {"orange", 5}
newset1 = {5.5}

# First way
thisset.update(newset)
thisset.update(newset1)

? Output: {'banana', 5, 'apple', 5.5, 'orange'}
# Second way
thisset.update(newset, newset1)
print(thisset)

? Output: {'banana', 5, 'apple', 5.5, 'orange'}

? Example 3: Add items and print them in sorted order
thisset = {"apple", "banana"}
newset = {"orange", 5}
newset1 = {5.5}
thisset.update(newset, newset1)
print(sorted(thisset, key=str))

? Output: [5, 5.5, 'apple', 'banana', 'orange']


! Add Any Iterable
* The object in the update() method does not have to be a set, it can be any
* iterable object (tuples, lists, dictionaries etc.).

? Example: Add elements of a list to at set:
thisset = {"apple", "banana"}
thislist = ["train", "bus"]

thisset.update(thislist)
print(thisset)

? Output: {'apple', 'train', 'bus', 'banana'}



"""
