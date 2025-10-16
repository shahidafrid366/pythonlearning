# 1. Grocery Budget Calculator
# TODO: Calculate monthly grocery examples
# Hint: Use float() for input and multiply weekly by 4

grocery1 = float(input("Enter grocery 1st price: "))
grocery2 = float(input("Enter grocery 2nd price: "))
grocery3 = float(input("Enter grocery 3rd price: "))

total = grocery1 + grocery2 + grocery3
total *= 4
print(f"Your monthly total is: {total}")
