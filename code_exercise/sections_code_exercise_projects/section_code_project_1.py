import random

# creating a program generates a random whole number

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

# returning result with randint
results = random.randint(lower_bound, upper_bound)

print(results)

