print(10/2)         # Division: Output 5.0
print(10//2)        # Division: Output 5

print(10 * 2)       # Multiplication: Output 20

print(10 ** 2)      # Output: 100 base ** exponent operation like square, cube, etc

# Modulo operation
# dividend % divisor = Remainder
print(10 % 3)       # Output: 1
print(15 % 4)       # Output: 3

# Calculate 3 to the power of 4, and find the remainder when dividend by 5
# print(3 ** 4)             # 3 to power of 4 = 81
remainder = (3 ** 4) % 5
print(remainder)            # Remainder = 1


# Calculate the volume of cube
# 1. Store the length of cube's side (let's say that its 4 units)
# 2. Calculate the volume using formula (volume = side length * side length)
# 3. print the results
side_length = 4
volume = side_length ** 3
print(f"Volume of cube = {volume}")
