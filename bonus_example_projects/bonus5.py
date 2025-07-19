# create a program that output this list
waiting_list = ["sen", "john", "ben"]



# putting amy wn twist on it. allowing user to enter a name
list_input = input("Enter a name: ")
waiting_list.append(list_input)

waiting_list.sort()
# will sort into alphabetically
# outputs
#1.Ben
#2.John
#3.Sen

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.title()}"
    print(row)

