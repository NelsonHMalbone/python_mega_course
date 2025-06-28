meals = ["pasta", "pizza", "salad"]

for meal in meals:
    meal = meal.capitalize()
    print(meal)


for text in 'nelson':
    text = text.capitalize()
    print(text)



name = 'malbone'
for i in range(1, len(name) + 1):
    print(name[:i])


# center pyramid
for i in range(1, len(name) + 1):
    spaces = " " * (len(name) - i)
    print(spaces + name[:i])


rows = 6
# left aligned
for i in range(1, rows + 1):
    print("*" * i)

# centered
for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    stars = '*' * (2 * i - 1) # calculates how many * to place on a line
    print(spaces + stars)

# inverted
for i in range(rows, 0 , -1):
    spaces = " " * (rows - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

# right aligned inverted
for i in range(rows, 0, - 1):
    stars = "*" * (2 * i - 1)
    print(stars)

# right aligned
for i in range(1, rows + 1):
    stars = "*" * (2 * i + 1)
    print(stars)