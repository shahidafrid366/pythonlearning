"""
! The try block lets you test a block of code for errors.
! The except block lets you handle the error.
! The else block lets you execute code when there is no error.
! The finally block lets you execute code, regardless of the result of the try- and except blocks.

! Exception Handling
* When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
* These exceptions can be handled using the try statement.

? Example:
The try block will generate an exception, because x is not defined:

try:
    print(x)
except:
    print("An exception occurred")


* Since the try block raises an error, the except block will be executed.
* Without the try block, the program will crash and raise an error:

? Example: This statement will raise an error, because x is not defined
print(x)    # Error: NameError: name 'x' is not defined


! Many Exceptions
* You can define as many exception blocks as you want, e.g. if you want to execute a special block of code
* for a special kind of error

? Example: Print one message if the try block raises a NameError and another for other errors
#The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

? Output: Variable x is not defined


!! Built-in Exceptions in Python
The table below shows built-in exceptions that are usually raised in Python:

* Exception	            Description
* -------------         ------------
ArithmeticError	        Raised when an error occurs in numeric calculations
AssertionError	        Raised when an assert statement fails
AttributeError	        Raised when attribute reference or assignment fails
Exception	            Base class for all exceptions
EOFError	            Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError	    Raised when a floating point calculation fails
GeneratorExit	        Raised when a generator is closed (with the close() method)
ImportError	            Raised when an imported module does not exist
IndentationError	    Raised when indentation is not correct
IndexError	            Raised when an index of a sequence does not exist
KeyError	            Raised when a key does not exist in a dictionary
KeyboardInterrupt	    Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError	            Raised when errors raised cant be found
MemoryError	            Raised when a program runs out of memory
NameError	            Raised when a variable does not exist
NotImplementedError	    Raised when an abstract method requires an inherited class to override the method
OSError	                Raised when a system related operation causes an error
OverflowError	        Raised when the result of a numeric calculation is too large
ReferenceError	        Raised when a weak reference object does not exist
RuntimeError	        Raised when an error occurs that do not belong to any specific exceptions
StopIteration	        Raised when the next() method of an iterator has no further values
SyntaxError	            Raised when a syntax error occurs
TabError	            Raised when indentation consists of tabs or spaces
SystemError	            Raised when a system error occurs
SystemExit	            Raised when the sys.exit() function is called
TypeError	            Raised when two different types are combined
UnboundLocalError	    Raised when a local variable is referenced before assignment
UnicodeError	        Raised when a unicode problem occurs
UnicodeEncodeError	    Raised when a unicode encoding problem occurs
UnicodeDecodeError	    Raised when a unicode decoding problem occurs
UnicodeTranslateError	Raised when a unicode translation problem occurs
ValueError	            Raised when there is a wrong value in a specified data type
ZeroDivisionError	    Raised when the second operator in a division is zero



"""
