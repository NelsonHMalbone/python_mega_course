date = input("Enter the date (ex.2020-20-09): ")
time = input("Enter the time (24 Hr or 12 Hr): ")
mood_rating = input("Enter your mood 1 - 10: ")
thoughts = input("Let the thoughts flow:\n")

# creating a file using the date as the filename
with open(f"../bonus_example_projects/Journal/{date}.txt", "w") as file:
    file.write(time + "\n")
    file.write(mood_rating + "\n")
    file.write(thoughts)