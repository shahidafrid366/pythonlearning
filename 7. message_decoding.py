# Task: Decoded message

# You've just intercepted the encoded message
# The message is a string of numbers, but you know their encryption method.
# Each letter of alphabet is represented by its position [A=0, B=1,...,Z=25] and these numbers are
# concatenated into one long string. You need to decode the last letter of this secret message

# 1. Extract the last digit of encode message
# 2. Use this to determine the corresponding letter
# 3. Report back with decoded letter

encoded_message = 1235432564221

# Revealing the last letter
last_digit = encoded_message % 26

# Revealing the last letter
decoded_letter = chr(last_digit + 65)           # ASCII character for capital A starts from 65
print(f"The last letter of the secret message is: {decoded_letter}")
