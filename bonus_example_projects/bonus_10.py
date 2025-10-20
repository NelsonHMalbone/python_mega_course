# creating a area caluclator
try:
    length = float(input("enter a length: "))
    width = float(input("enter a width: "))
    if length == width:
        print("This is a square try again")
    else:
        area = length * width

        print(area)
except ValueError:
    print("Please enter a number")