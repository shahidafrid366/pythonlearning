"""
! Frozen Set
* frozenset is an immutable version of a set.
* The elements inside must be hashable (so you cannot put lists or other sets inside).
* Like sets, it contains unique, unordered, unchangeable elements.
* Unlike sets, elements cannot be added or removed from a frozenset.


! Creating a frozenset
* Use the frozenset() constructor to create a frozenset from any iterable.

? Example: Create a frozenset and check its type:
x = frozenset({"apple", "orange", "mango"})
print(x)                # frozenset({'apple', 'orange', 'mango'})
print(type(x))          # <class 'frozenset'>


! Frozenset Methods
* Being immutable means you cannot add or remove elements. However, frozensets support all
* non-mutating operations of sets.

!Method	                Shortcut	Description
? --------------------  --------    -----------
copy()	 	                        Returns a shallow copy
difference()	        -	        Returns a new frozenset with the difference
intersection()	        &	        Returns a new frozenset with the intersection
isdisjoint()	 	                Returns whether two frozensets have an intersection
issubset()	            <= / <	    Returns True if this frozenset is a (proper) subset of another
issuperset()	        >= / >	    Returns True if this frozenset is a (proper) superset of another
symmetric_difference()	^	        Returns a new frozenset with the symmetric differences
union()	                |	        Returns a new frozenset containing the union

------

! copy()
* Even though frozenset is immutable, it has a .copy() method for API consistency with sets.
* For a frozenset, .copy() just returns itself (not a new object) because there’s no point in
* duplicating immutable data.

? Example:
a = frozenset({"a", 1, 4.5})
x = a.copy()
print(f"a = {a}")       # a = frozenset({1, 'a', 4.5})
print(f"x = {x}")       # x = frozenset({1, 'a', 4.5})

------

! difference()
* The difference operation means: “Give me all the elements in Set A that are not in Set B.”

? Example:
x = frozenset({1, "a", 4.5, 9})
y = frozenset({1, 2, "Shahid"})

print(y.difference(x))              # frozenset({2, 'Shahid'})
print(x - y)                        # frozenset({9, 4.5, 'a'})

? So:
* y.difference(x) → elements in y but not in x.
* Similarly, x.difference(y) → elements in x but not in y.
* The operator form x - y is exactly the same as x.difference(y).

------

! intersection()
* The intersection between two sets means: "Give me only the elements that are common to both sets."

* A.intersection(B) → elements present in both A and B.
* You can also use the & operator: A & B.

? Example:
x = frozenset({1, "a", 4.5, 9, 3})
y = frozenset({1, 2, "Shahid", 3})

print(x & y)                # frozenset({1, 3})

------

! isdisjoint()
* The method A.isdisjoint(B) checks if two sets have no common elements.
* It returns:
    * True → if they are completely separate (no overlap).
    * False → if they share at least one element.

? Think of it as asking:
    “Are these two sets disjoint (non-overlapping)?”

? Example:
x = frozenset({1, "a", 4.5, 9, 3})
y = frozenset({1, 2, "Shahid", 3})

print(x.isdisjoint(y))          # False

------

! issubset()
* A.issubset(B) checks if all elements of set A are also present in set B.
* It answers the question: “Is A completely contained inside B?”
* Returns:
    * True → if every element in A is inside B.
    * False → if at least one element in A is missing in B.

? Example:
x = frozenset({1, 2})
y = frozenset({1, 2, 3, 4})

print(x.issubset(y))  # Is x inside y?  Output: True
print(y.issubset(x))  # Is y inside x?  Output: False

Step 1: Compare x.issubset(y)
x = {1, 2}
y = {1, 2, 3, 4}

Are all elements of x in y?
    1 → in y ✅
    2 → in y ✅
    Yes, so → True

Step 2: Compare y.issubset(x)
y = {1, 2, 3, 4}
x = {1, 2}

Are all elements of y in x?
    3 → not in x ❌
    4 → not in x ❌
    So → False

* You can also use the operator <= (less than or equal)
* And a proper subset check with < (strict)

------

! superset()
* A.issuperset(B) checks if all elements of set B are also present in set A.
* In other words: “Does A completely contain B?”

* It is the reverse of issubset().
* If A.issubset(B) is True, then B.issuperset(A) will also be True.

? Exmaple:
x = frozenset({1, 2})
y = frozenset({1, 2, 3, 4})

print(x.issuperset(y))  # Is x a superset of y?     Output: False
print(y.issuperset(x))  # Is y a superset of x?     Output: True

Step 1: x.issuperset(y)
    x = {1, 2}
    y = {1, 2, 3, 4}
    Is y fully inside x?
    No, because y has 3 and 4 that are missing in x.
    ✅ Result: False

Step 2: y.issuperset(x)
    y = {1, 2, 3, 4}
    x = {1, 2}
    Is x fully inside y?
    Yes, because 1 and 2 are in y.
    ✅ Result: True

* You can also use the operator >= (greater than or equal):
* And a proper superset check with > (strict):

------

! symmetric_difference()?

* The symmetric difference between two sets means:
* “Give me all the elements that are in either of the sets, but not in both.”

* Think of it as exclusive OR (XOR) for sets.
* A.symmetric_difference(B) = (A ∪ B) − (A ∩ B)

* You can also use the ^ operator

? Example:
x = frozenset({1, 2, 3, "a"})
y = frozenset({2, 3, 4, "b"})

print(x.symmetric_difference(y))    # Output: frozenset({1, 'a', 4, 'b'})
print(x ^ y)                        # Output: frozenset({1, 'a', 4, 'b'})

? Step-by-step check
    x = {1, 2, 3, "a"}
    y = {2, 3, 4, "b"}

Now compare elements:
Common elements (present in both): {2, 3} → ❌ exclude these.

Leftover unique elements:
From x: {1, "a"}
From y: {4, "b"}

Combine them → {1, "a", 4, "b"}

"""
