"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

! File Handling
The key function for working with files in python is open() function
The open() takes two parameters: filename & mode

There are four different methods (modes) for opening a file:
    1. "r" - Read - Default value. Opens a file for reading, error if the files does not exist
    2. "a" - Append - Opens a file for appending, creates the file if it does not exist
    3. "w" - Write - Opens a file for writing, creates the file if it does not exist
    4. "x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
    "t" - Text - Default value. Text mode
    "b" - Binary - Binary mode (e.g. images)


Syntax: To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")

The code above is the same as: f = open("demofile.txt", "rt")
Because "r" for read, and "t" for text are the default values, you do not need to specify them.

Note: Make sure the file exists, or else you will get an error.



"""
