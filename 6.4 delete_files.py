"""
To delete a file, you must import the OS module, and run its os.remove() function

Example:
import os
os.remove("abc.txt")


Check if File exist
-------------------
To avoid getting an error, you might want to check if the file exists before you try to delete it

Example: Check if file exists, then delete it
import os

if os.path.exists("abc.txt"):
    os.remove("abc.txt")
else:
    print("file does not exists")



Delete Folder
--------------
To delete an entire folder, use the os.rmdir() method

Example: Remove the entire folder
import os

os.rmdir("myfolder")

Note: You can only remove empty folders.

"""
