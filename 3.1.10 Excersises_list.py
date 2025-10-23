# What will be the result of following syntax:
mylist = ["apple", "banana", "cherry"]
print(mylist[1])  # Output: banana


# What will be the result of the following syntax:
mylist = ["apple", "banana", "banana", "cherry"]
print(mylist[2])  # Output: banana


# True or False.
# List items cannot be removed after the list has been created.
# Answer: False


# Select the correct function for returning the number of items in a list:

# thislist = ['apple', 'banana', 'cherry']
# print(________(thislist))
# Answer: len -------->  print(len(thislist))


# What will be the result of the following syntax:
mylist = ["apple", "banana", "cherry"]
print(mylist[-1])  # cherry


# Print the second item in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# print(_______)
# Answer: print(fruits[1])


# What will be the result of the following syntax:
mylist = ["apple", "banana", "cherry", "orange", "kiwi"]
print(mylist[1:4])  # ['banana', 'cherry', 'orange']


# Use a range of indexes to print the third, fourth, and fifth item in the list.
# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[___])
# Answer: print(fruits[2:5])


# What will be the result of the following syntax:
mylist = ["apple", "banana", "cherry"]
mylist[0] = "kiwi"
print(mylist[1])  # Output: banana


# Change the value from "apple" to "kiwi", in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# ______ = ______

# Answer: fruits[0] = "kiwi"


# What will be the result of the following syntax:
mylist = ["apple", "banana", "cherry"]
mylist[1:2] = ["kiwi", "mango"]
print(mylist[2])  # Output: mango


# What will be the result of the following syntax:
mylist = ["apple", "banana", "cherry"]
mylist.insert(0, "orange")
print(mylist[1])  # apple


# Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)


# Use the insert method to add "lemon" as the second item in the fruits list.
# fruits = ["apple", "banana", "cherry"]
# __________ "lemon")

# Output:
# fruits = ["apple", "banana", "cherry"]
# fruits.insert(2, ("lemon"))


# Fill the missing parts to add the elements of tropical to fruits:
# fruits = ['apple', 'banana', 'cherry']
# tropical = ['mango', 'pineapple', 'papaya']
# _______ . _________ (_______)
# Answer:
# fruits = ['apple', 'banana', 'cherry']
# tropical = ['mango', 'pineapple', 'papaya']
# fruits.extend(tropical)


# What is the List method for removing list items?
# Answer: pop()


# Use the remove method to remove "banana" from the fruits list.
# fruits = ["apple", "banana", "cherry"]
# ______._______(________)
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")


# What will be the result of the following syntax:
mylist = ["apple", "banana", "cherry"]
mylist.pop(1)
print(mylist)  # Output: ['apple', 'cherry']


# Select the correct function to remove all items from a list:
# fruits = ['apple', 'banana', 'cherry']
# fruits.______
# Answer:
fruits = ["apple", "banana", "cherry"]
fruits.clear()


# Create a list of 5 fruits and print each fruit using a loop.
fruits = ["apple", "banana", "orange", "cherry", "pine apple"]
for f in fruits:
    print(f)

# Add a new fruit to the list using append() and print the updated list.
fruits1 = ["apple", "banana", "orange", "cherry", "pine apple"]
fruits1.append("berries")
print(fruits1)

# Use extend() to add multiple fruits to the list.
fruits_old = ["apple", "banana", "orange", "cherry", "pine apple"]
fruits_old.extend(["kiwi", "guava"])
print(fruits_old)

# Remove a fruit from the list using remove() and print the list.
fruits2 = ["apple", "banana", "orange", "cherry", "pine apple"]
fruits2.remove("cherry")
print(fruits2)

# Find the index of a specific fruit using index().
fruits3 = ["apple", "banana", "orange", "cherry", "pine apple"]
print(fruits3.index("orange"))

# Count how many times a fruit appears using count().
fruits4 = ["apple", "banana", "orange", "cherry", "pine apple", "banana"]
count = fruits4.count("banana")

# Reverse the list using reverse() and print it.
fruits5 = ["apple", "banana", "orange", "cherry", "pine apple"]
fruits5.reverse()
print(fruits5)

# Sort the list alphabetically using sort().
fruits6 = ["apple", "banana", "orange", "cherry", "pine apple"]
fruits6.sort()
print(fruits6)

# Create a list of numbers and find the sum, max, and min values.
numbers = [1, 2, 3]
print(sum(numbers))
print(max(numbers))
print(min(numbers))

# Use slicing to print the first 3 elements of a list.
nums1 = [1, 2, 3, 4, 5, 6, 7]
print(nums1[0:3])

# Use slicing to reverse a list.
nums2 = [1, 2, 3, 4, 5, 6, 7]
print(nums2[::-1])

# Create a nested list and access elements inside the inner list.
nested_nums_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(nested_nums_list[1][0])  # 3

# Write a program to remove duplicates from a list.
# There are two approaches to solve this
# Approach 1
duplicte_list = [1, 1, 3, 2, 5, 6, 7, 7, 5, 4]
unique_list = list(set(duplicte_list))
print(unique_list)

# Approach 2
duplicte_list = [1, 1, 3, 2, 5, 6, 7, 7, 5, 4]
unique_list = []
for x in duplicte_list:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)

# Write a program to merge two lists without using + operator.
first_list = [1, 2, 3]
second_list = [4, 5, 6]
first_list.extend(second_list)
print(first_list)

# Write a program to find the second largest number in a list.
# We have couple of ways to solve this program
# This approach will print the second largest number if the order is in ascending
second_largest_num = [1, 2, 3, 4]
second_largest_num.reverse()
print(second_largest_num[1])

# This approach will use the sorted() to solve this problem
num_list = [3, 4, 1, 2]
sorted_nums = sorted(num_list, reverse=True)  # Output: [4, 3, 2, 1]
second_largest = sorted_nums[1]
print(second_largest)

# This approach will use the set() to remove duplicates and print the second largest number
num_list = [3, 4, 3, 1, 1, 2]
unique_nums = list(set(num_list))  # Removes Duplicates
unique_nums.sort(reverse=True)  # Sorts Descending
second_large_num = unique_nums[1]
print(second_large_num)

# Write a program to check if a list is empty.
# Approach 1:
empty_list = []

if len(empty_list) == 0:
    print("list is empty")
else:
    print("list is not empty")

# Approach 2:
empty_list = []

if not empty_list:
    print("list is empty")
else:
    print("list is not empty")
