"""
! Join Sets
* There are several ways to join two or more sets in Python.
    - The union() and update() methods joins all items from both sets.
    - The intersection() method keeps ONLY the duplicates.
    - The difference() method keeps the items from the first set that are not in the other set(s).
    - The symmetric_difference() method keeps all items EXCEPT the duplicates.


! union()
The union() method returns a new set with all items from both sets.

? Example: Join set1 and set2 into a new set:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

? Output: {'c', 1, 2, 'b', 3, 'a'}

---
* You can use pipe | instead of union() method and you will get the same result

? Example:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

? Output: {'c', 1, 2, 'a', 3, 'b'}

---

! Join Multiple Sets
* All the joining methods and operators can be used to join multiple sets.
* When using a method, just add more sets in the parentheses, separated by commas:

? Example 1: Join multiple sets with the union() method:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

? Output: {1, 2, 'c', 3, 'bananas', 'a', 'cherry', 'apple', 'b', 'Elena', 'John'}

------
When using the | operator, separate the sets with more | operators:

? Example 2: Use | to join two sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

? Output: {1, 2, 'c', 3, 'bananas', 'a', 'cherry', 'apple', 'b', 'Elena', 'John'}


! Join a Set and a Tuple
* The union() method allows you to join a set with other data types, like lists or tuples.
* The result will be a set.

? Example: Join a set with a tuple
set1 = {"a", "b", "c"}
set2 = (1, 2, 3)

myset = set1.union(set2)
print(myset)

? Output: {1, 2, 3, 'c', 'b', 'a'}

! Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.

-----

! update()
* The update() method inserts all items from one set to another
* The update() changes the original set, and does not return a new set

? Example: The update() method inserts the items in set2 into set1:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

? Output: {1, 2, 3, 'a', 'c', 'b'}

! Note: Both union() and update() will exclude any duplicate items.

"""
