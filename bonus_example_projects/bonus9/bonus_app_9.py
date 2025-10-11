# nelson malbone date 10/10/2025 udemy bonus project
# get user to input a new password
from unicodedata import digit


password_input = input("Enter new password: ")

# result list for password
result = {}

# checking against conditions
# chars 8 or greater

if len(password_input) >= 8:
    result["length: "] = True
else:
    result["length: "] = False

# checking if number is in string
digit = False
for i in password_input:
    if i.isdigit():
        digit = True

result["digit: "] = digit

# checking to see if there is a uppercase char
upper_char = False
for x in password_input:
    if x.isupper():
        upper_char = True

result["upper: "] = upper_char

# getting the strong or weak password
# using all function

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak password")

# at this point we are finished, but now we are going to switch it all over to dictionaries
# so now we can see what's true and not true
