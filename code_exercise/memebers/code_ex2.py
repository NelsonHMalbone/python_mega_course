user_input = input("Enter new member name: ") + "\n"

file = open("members.txt", 'r')
member_list = file.readlines()
file.close()

member_list.append(user_input)
file = open("members.txt", "w")
file.writelines(member_list)
file.close()
