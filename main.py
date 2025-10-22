print("Lessons Learn Tracker")
# Prompts for project
prompt_user_text = "Enter your lesson Learned: " # variable to store message
prompt_user_text1 = "Would you like to add, show, edit, complete, exit (select one):  "

# list method
#lesson_list = {} # don't need this because we are reading file now

def get_lesson():
    with open('lesson_learn.txt', 'r') as file_local:
        # equal to writeline but just reading
        lesson_list_local = file_local.readlines()  # list was created here
    return lesson_list_local


while True:
    user_decision = input(prompt_user_text1).strip()
    user_decision = user_decision.strip()

    if user_decision.startswith("add"):
        user_text = user_decision[4:]

        lesson_list = get_lesson()

        # optional_note = input( Add a quick note (optional): )
        lesson_list.append(user_text + '\n')

        with open('lesson_learn.txt','w') as file:
            file.writelines(lesson_list)

    elif user_decision.startswith("show"):
        lesson_list = get_lesson()

        # list comprehensions  way
        # new_lesson_list = [item.strip("\n") for item in lessons]

        for index, item in enumerate(lesson_list):
            # direct method
            item = item.strip("\n")
            row = f'{index + 1}: {item}' # starts list at 1
            print(row)

    elif user_decision.startswith("edit"):
        try:
            # making it so the user just has to do edit 1 or 2 or whatever number
            number = int(user_decision[4:])
            number = number - 1

            with open('lesson_learn.txt', 'r') as file:
                # equal to writeline but just reading
                lesson_list = file.readlines() # list was created here

            new_lesson = input("Enter a new lesson: ")
            lesson_list[number] = new_lesson + '\n'

            with open('lesson_learn.txt','w') as file:
                file.writelines(lesson_list)
        except ValueError:
            print("please use a number to select which item to edit (ex: edit 1)")
            continue

    elif user_decision.startswith("complete"):
        try:
            try:
                number = int(user_decision[8:])

                # getting current list
                with open('lesson_learn.txt', 'r') as file:
                    # equal to writeline but just reading
                    lesson_list = file.readlines() # list was created here

                lesson_to_remove = lesson_list[number - 1].strip("\n")
                removed = lesson_list.pop(number - 1) # removes the number selected
                with open('lesson_learn.txt','w') as file:
                    file.writelines(lesson_list)
                print(f'out of lesson list: {lesson_to_remove} was removed')
            except ValueError:
                print("please use a number to select which item to edit (ex: complete 1)")
                continue
        except IndexError:
            print("Out of range")
            continue
    elif "exit" in user_decision:
        break

    else:
        print("command not a valid")
print("Goodbye")
