"""
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content


Example: Open the file "demofile.txt" and append content to the file
with open("demofile.txt", "a") as f:
    f.write("\nAdding new line to the file")

# Open and read the file after appending
with open("demofile.txt") as f:
    print(f.read())


Overwrite Existing Content
---------------------------
To overwrite the existing content to the file, use the w parameter

Example:
with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content")

# Open and reading the file after overwriting
with open("demofile.txt") as f:
    print(f.read())

Note: the "w" method will overwrite the entire file.



Create a new file
-----------------
To create a new file in Python, use the open() method, with one of the following parameters:
"x" - Create - will create a file, returns an error if the file exists
"a" - Append - will create a file if the specified file does not exists
"w" - Write - will create a file if the specified file does not exist

Example: Create a new file called "myfile.txt"
f = open("myfile.txt", "x")
Result: a new empty file is created.

Note: If the file already exist, an error will be raised.

while creating a file with open(), in the second argument you can make use of several options like:
 "r" (read), "w" (write), "x" (Create only), "a" (append only), "b" (Binary mode), "t" (Text mode (default))

these arguments can also be combined with other modes like "rb", "wb", "ab", "r+b" or "rb+", "a+b" or "ab+", "wt", etc


"""
