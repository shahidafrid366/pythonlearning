"""
return is both 'statement' & 'keyword'

1. A return statement is used to end the execution of the function call and
   it "returns" the value of the expression following the return keyword to the caller.
2. The statements after the return statements are not executed.
3. If the return statement is without any expression, then the special value None is returned.
4. A return statement is overall used to invoke a function so that the passed statements
   can be executed.
5. Return statement should be the last in function, bcoz it terminates the program
6. return keyword is used only in functions
7. datatype of return value can be anything (integer, string, tuple, list, etc.)

Syntax:
-------
def function_name(parameters):
    # Function body
    return value

When the return statement is executed, the function terminates and the specified value
is returned to the caller. If no value is specified, the function returns None by default.

Note: Return statement can not be used outside the function.


Let's see below example program for better understanding:
# Declaring variables to calculate simple interest
principal = 10000
num_of_years = 3
rate_of_intrest = 9.8

# Defining function
def simple_interest(principal, num_of_years, rate_of_intrest):  # passing three values
    si = (principal + num_of_years + rate_of_intrest) / 100     # si is local variable inside the function
    print(f"Simple Interest {si}")                              # printing
    # print("Simple Interest ", si)

simple_interest(principal, num_of_years, rate_of_intrest)

This program prints the simple interest. but if you print si variable it outside it will
throw error since si acts as local variable here.

So here comes the concept of return statements.
From above program if you want to access the si variable/value you have to use return statement

# Declaring variables to calculate simple interest
principal = 10000
num_of_years = 3
rate_of_intrest = 9.8

# Defining function
def simple_interest(principal, num_of_years, rate_of_intrest):
    si = (principal + num_of_years + rate_of_intrest) / 100
    print(f"Simple Interest {si}")
    return si  # using return statement

si = simple_interest(principal, num_of_years, rate_of_intrest)  # return value is stored si variable outside the function
print(si)  # printing the returned by function
total_payment = principal + si
print(total_payment)


## You can return multiple values
def add(a, b):
    sum = a + b
    sub = a - b
    return sum, sub
add(2,3)

# This will give output but it doesn't print out in console unless you assign it to variable
# TODO that we should do like this
def add(a, b):
    sum = a + b
    sub = a - b
    return sum, sub

result = add(2, 3)  # This prints the result but in tuple format (5, -1)
print(result)

# To print in expected format like sum: 5 & sub: -1 you should assign it like this
sum, sub = add(2, 3)
print(sum)
print(sub)
"""
