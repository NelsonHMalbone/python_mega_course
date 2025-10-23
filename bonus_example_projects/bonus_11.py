# taking the data in the txt file of the data folder will making a script to calculate the average temp
from os import remove


def get_temps_average():
    with open("bonus11_ex/data.txt", "r") as file:
        data = file.readlines() # will read for list
    values = data[1:]
    # updating list to numbers instead of strings
    values = [float(i) for i in values]
    averages = sum(values) / len(values)

    return averages

average = get_temps_average()
print(f'{average:.2f}')