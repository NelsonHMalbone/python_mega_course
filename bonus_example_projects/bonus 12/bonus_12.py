# using this for bonus 13 also
from modules.utils import parse, convert


feet_inches = input("enter feet and inches: ")

# in bonus 13 we discover this function is doing to much doing more then one thing
# does the parsing and conversion


feet_inches_tuple = parse(feet_inches)
print("fi", feet_inches_tuple)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])


if result < 1:
    print("Kid to small")
else:
    print("kid can use the slide")