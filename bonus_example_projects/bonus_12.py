# using this for bonus 13 also

feet_inches = input("enter feet and inches: ")

# in bonus 13 we discover this function is doing to much doing more then one thing
# does the parsing and conversion

def parse(feet_inches):
    split_convert = feet_inches.split(" ")
    feet = float(split_convert[0])
    inch = float(split_convert[1])
    return feet, inch

def convert(feet, inch):
    meters = feet * 0.3048 + inch * 0.0254
    return meters

feet_inches_tuple = parse(feet_inches)
print("fi", feet_inches_tuple)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])


if result < 1:
    print("Kid to small")
else:
    print("kid can use the slide")