# Calculate gallons of paint required
# TODO: Use different roundings methods (round up, round down and use round near).
# TODO: Create a custom rounding to nearest integer, multiply by 2, round to nearest integer then
# divide by 2 ( 'round()' custom rounding to nearest half of the gallon)
# TODO: Use the '.2.f' format specifier showing 2 decimals places
# Hint: Divide the total wall area by paint coverage per gallon. Use 'math' module.
# 'math.ceil()' rounds up to nearest integer,
# 'math.floor' rounds down to nearest integer.
# 'round()' rounds to nearest integer (0.5 rounds up to 1)

import math

# Get the input from user
wall_area = float(input("Enter the wall area in square feet: "))
paint_coverage = float(input("Enter the paint coverage per gallon: "))
paint_needed = wall_area / paint_coverage

# Different rounding methods
# math.ceil()  - rounds up to nearest integer
ceil_round = math.ceil(paint_needed)

# math.floor()  - rounds down to nearest integer
floor_round = math.floor(paint_needed)

# round()  - rounds to nearest integer
normal_round = round(paint_needed)

# Custom rounding to the nearest half gallon
# multiply by 2 and round to nearest integer, then divide by 2
round_to_half = round(paint_needed * 2) / 2

# printing the results
# using .2f format specifier shows 2 decimals after float value.
print(f"Exact amount {paint_needed:.2f} gallons of paint")
print(f"Rounded up (ceiling) {ceil_round} gallons")
print(f"Rounded down (floor) {floor_round} gallons")
print(f"Normal round {normal_round} gallons")
print(f"Rounded to nearest half gallon : {round_to_half:.1f} gallons")

