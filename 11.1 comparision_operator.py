"""
Comparision operator always returns boolean values: True or False

We have 10 comparision operators in Python

<       : less than
<+      : less than or equal
>       : greater than
>=      : greater than or equal
==      : equal
!=      : not equal
is      : object identity
is not  : negated object identity
in      : membership
not in  : negated membership


"""

receipt_number = 2233

try:
    slices = int(input("Enter no of slices you need: "))
    price_per_slice = int(input("Enter the price per slice: "))

    total = slices * price_per_slice

    print(total == receipt_number)

except ValueError:
    print("Enter valid input in numeric")
