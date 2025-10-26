feet_inches = input("enter feet and inches: ")

def convert(feet_inches):
    split_convert = feet_inches.split(" ")
    feet = float(split_convert[0])
    inch = float(split_convert[1])

    meters = feet * 0.3048 + inch * 0.0254
    return meters

result = convert(feet_inches)

if result < 1:
    print("Kid to small")
else:
    print("kid can use the slide")