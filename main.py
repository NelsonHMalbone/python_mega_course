print("Lessons Learn Tracker")
# Prompts for project
prompt_user_text = "Enter your lesson Learned: " # variable to store message
prompt_user_text1 = "Would you like to add, show, edit, complete, exit (select one):  "

# list method
# lesson_list = [] # dont need this because we are reading file now

while True:
    user_decision = input(prompt_user_text1).strip()
    user_decision = user_decision.strip()
    match user_decision:
        case "add"|"a":
            user_text = input(prompt_user_text) + '\n'
            # read file to bebale to see the in console
            file = open('lesson_learn.txt', 'r')
            # equalivant to wrieline but just reading
            lesson_list = file.readlines()
            # need to close file so different code cant affect file
            file.close()
            # optional_note = input("Add a quick note (optional): ")
            lesson_list.append(user_text.capitalize())
            file = open('lesson_learn.txt','w')
            file.writelines(lesson_list)
            file.close()
        case "show"|"s":
            for index, item in enumerate(lesson_list):
                row = f'{index + 1}:{item}' # starts list at 1
                print(row)

        case "edit"|"e":
            number = int(input("number of lesson to edit: "))
            number = number - 1
            new_lesson = input("Enter a new lesson: ")
            lesson_list[number] = new_lesson

        case "complete":
            number = int(input("number of lesson to that are completed: "))
            removed = lesson_list.pop(number - 1) # removes the number selected
            print(f'out of lesson list {removed} was removed')

        case "exit"|"x":
            print("Goodbye")
            break
