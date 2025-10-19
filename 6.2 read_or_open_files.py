"""
Assume we have the following file, located in the same folder as Python:

demofile.txt
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck!

To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:

Example:
f = open("demofile.txt")
print(f.read())

If the file is located in a different location, you will have to specify the file path, like this:
Example: Open a file on a different location:
f = open("D:\\myfiles\welcome.txt")
print(f.read())

There are several way of opening a file in python:
f = open("demofile.txt")
f = open(
    "C:\\Users\\ShaikShahidAfrid\\Downloads\\python scripting\\PythonLearning\\demofile.txt"
)
f = open(
    r"C:\\Users\\ShaikShahidAfrid\\Downloads\\python scripting\\PythonLearning\\demofile.txt"
)
f = open(
    "C:/Users/ShaikShahidAfrid/Downloads/python scripting/PythonLearning/demofile.txt"
)
print(f.read())



Using with statement:
---------------------
You can also use the with statement when opening a file:

Example: Using the with keyword
with open("demofile.txt") as f:
    print(f.read())

Then you do not have to worry about closing your files, the with statement takes care of that.



Close Files:
------------
It is a good practice to always close the file when you are done with it.
If you are not using the with statement, you must write a close statement in order to close the file:

Example: Close the file when you are finished with it
f = open("demofile.txt")
    print(f.readline())
f.close()

Note: You should always close your files. In some cases, due to buffering, changes made to a file may not show until you close the file.



Read Only Parts of the File:
----------------------------
By default the read() method returns the whole text, but you can also specify how many characters you want to return

Example: Return the 5 first characters of the file
f = open("demofile.txt")
    f.read(5)
f.close()



Read Lines:
-----------
You can return one line by using the readline() method

Example: Read one line of the file
with open("demofile.txt") as f:
    print(f.readline())

By calling readline() two times, you can read the two first lines:
Example: Read two lines of the file
with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())
Output: With first print statement it will print 1st line & with second print statement it will print second line since pointer is at end of first line


By looping through the lines of the file, you can read the whole file, line by line:
Example:
with open("demofile.txt") as f:
    for x in f:
        print(x)



Pythons file objects (like f in your example) come with several methods that allow you to interact with files in different ways.
Here are list of the most commonly used file methods:

-> Reading Methods
f.read()        Reads the entire file content as a single string.
f.readline()    Reads one line at a time.
f.readlines()   Reads all lines and returns a list of strings.

-> Writing Methods
f.write(string)         Writes a string to file.
f.writelines(list)      Writes a list of strings to the file.

-> File Positioning
f.tell()                Returns current file position (in bytes).
f.seek(offset)          Moves the file pointer to a specific position.

-> File Status
f.closed                Returns True if the file is closed
f.mode                  Returns the mode in which the file was opened('r', 'w', etc).
f.name                  Returns the name of file

-> Closing
f.close()               Closes the file manually (not needed if using with)

In addition to the commonly used file methods (above ones) there are several other methods and attributes that are less commonly used but still useful depending on the context

f.flush()               Forces the write buffer to be written to disk immediately. Useful when writing to files in real-time
f.truncate(size=None)   Resizes the file to the given size (default is current position).
f.detach()              Used with buffered I/O to detach the underlying raw stream.
f.fileno()              Returns the file descriptor (an integer) used by the operating system.
f.isatty()              Returns True if the file is connected to a terminal device (like stdin/stdout).
f.readable()            Returns True if the file can be read.
f.writable()            Retruns True is the file can be written to.
f.seekable()            Returns True if the file supports random access (i.e., seek() can be used)

f.name                  Name of the file.
f.mode                  Mode in which the file was opened ('r', 'w', 'rb', etc.).
f.closed                Boolean indicating whether the file is closed.
f.encoding              Encoding used to decode or encode the file (e.g., 'utf-8'). Only available in text mode.
f.newlines              Type of newline characters found in the file ('\n', '\r\n', etc.).



"""

# f = open("demofile.txt")
# print(f.readlines())
# f.seek(0, 1)
# print(f.read(50))
# f.close()
