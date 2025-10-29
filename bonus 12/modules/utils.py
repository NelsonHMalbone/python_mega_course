def parse(feet_inches):
    split_convert = feet_inches.split(" ")
    feet = float(split_convert[0])
    inch = float(split_convert[1])
    return feet, inch

def convert(feet, inch):
    meters = feet * 0.3048 + inch * 0.0254
    return meters
