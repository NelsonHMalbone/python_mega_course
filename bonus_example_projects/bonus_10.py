# creating a area caluclator
try:
    length = float(input("enter a length: "))
    width = float(input("enter a width: "))

    area = length * width

    print(area)
except ValueError:
    print("Please enter a number")