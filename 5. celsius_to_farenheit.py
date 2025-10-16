# Celsius to Fahrenheit converter
# This script converts temperature from Celsius to Fahrenheit and demonstrates various types
# and string manipulations

days_in_week = 7
celsius_temperature = 25.0 # Temperature to convert
pi = 3.14159 # Example of a float constant

greeting = "Hello! "
user_name = "Python learner"

is_summer = True

month = ["January", "February", "March"]

temp_scales = {"Celsius" : "C", "Fahrenheit" : "F", "Kelvin" : "K"}

celsius_to_fahrenheit_factor = 9/5
fahrenheit_offset = 32

fahrenheit_temp = (celsius_temp * celsius_to_fahrenheit_factor) + fahrenheit_offset
fahrenheit_temp = round(fahrenheit_temp, 2)

full_greeting = greeting + user_name
print(full_greeting)
