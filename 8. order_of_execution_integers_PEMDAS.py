# Order of Execution
# Python follows PEMDAS order of execution while performing arithmatic operations

## PEMDAS
# 1. Parenthesis
# 2. Exponentiation
# 3. Multiplication, Division, Integer Division, Modulo
# 4. Addition, Substraction


# Example 1:
print(5+3 * 2)      # Output: 11
print((5+3) * 2)    # Output: 16
print(10-2 ** 2)    # Output: 6
print(20/4*2)       # Output: 10.0

# Example 2: Complex Expression
result = (10 + 5 * 2)  ** 2 - 30 / (2 + 1)      # Output: 390
# (10 + 5 * 2)  ** 2 - 30 / (2 + 1)
# (10 + 10) ** 2 - 30 / (2 + 1)    # Parenthesis is the first Priority and then multiplication here (PEDMAS)
# (20) ** 2 - 30 / 3               # Exponent is the next priority
# 400 - 30 / 3                     # Division is the next priority
# 400 - 10 = 390
print(result)
