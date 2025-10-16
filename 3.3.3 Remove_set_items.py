"""
! Remove Item
* To remove an item in a set, use the remove(), or the discard() method.

? Example: Remove 'banana' by using remove() method
thisset = {"apple", "banana", "orange"}
thisset.remove("banana")
print(thisset)

? Output: {'orange', 'apple'}

* Note: If the item to remove does not exist, remove() will raise an error.
*       but by using discard() it won't raise an error.

? Example: Using remove method to demonstrate the error
thisset = {"apple", "cherry"}
thisset.remove("banana")
print(thisset)

? Output: Traceback (most recent call last):
# KeyError: 'banana'

? Example: Using discard method to demonstrate the error
thisset = {"apple", "cherry"}
thisset.discard("banana")
print(thisset)

? Output: {'cherry', 'apple'}
* Note: If the item to remove does not exist, discard() will NOT raise an error.

------

* You can also use the pop() method to remove an item, but this method will remove a random item,
* so you cannot be sure what item that gets removed.

* The return value of the pop() method is the removed item.

? Example: Remove a random item by using pop() method
thisset = {"apple", "banana", "cherry" }
x = thisset.pop()
print(x)            # Output: apple
print(thisset)      # Output: {'cherry', 'banana'}

! Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

------

! clear()
* The clear() method empties the set:

? Example:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

? Output: set()  # This returns the Empty set


! del
* The del keyword will delete the set completely:

? Example: Example demonstrating deleting a set
thisset = {"apple", "banana", "orange"}
del thisset
print(thisset)  # This will raise an error because the set no longer exists

? Output: Traceback (most recent call last): NameError: name 'thisset' is not defined

"""
