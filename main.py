print("Lessons Learn Tracker")
# Prompts for project
prompt_user_text = "Enter your lesson Learned: " # variable to store message
prompt_user_text1 = "Would you like to add, show, edit, complete, exit (select one):  "

# list method
#lesson_list = {} # don't need this because we are reading file now

while True:
    user_decision = input(prompt_user_text1).strip()
    user_decision = user_decision.strip()

    if "add" in user_decision:
        user_text = input(prompt_user_text) + '\n'

        with open('lesson_learn.txt', 'r') as file:
            # equal to writeline but just reading
            lesson_list = file.readlines() # list was created here



        # optional_note = input( Add a quick note (optional): )
        lesson_list.append(user_text.capitalize())
        with open('lesson_learn.txt','w') as file:
            file.writelines(lesson_list)

    if "show" in user_decision:
        with open("lesson_learn.txt", "r") as file:
            lessons = file.readlines()


        new_lesson_list = []

        for item in lessons:
            lessons_new = item.strip("\n")
            new_lesson_list.append(lessons_new)

        # list comprehensions  way
        # new_lesson_list = [item.strip("\n") for item in lessons]

        for index, item in enumerate(new_lesson_list):
            # direct method
            #item = item.strip("\n")
            row = f'{index + 1}: {item}' # starts list at 1
            print(row)

    if "edit" in user_decision:
        number = int(input("number of lesson to edit: "))
        number = number - 1

        with open('lesson_learn.txt', 'r') as file:
            # equal to writeline but just reading
            lesson_list = file.readlines() # list was created here

        new_lesson = input("Enter a new lesson: ")
        lesson_list[number] = new_lesson + '\n'

        with open('lesson_learn.txt','w') as file:
            file.writelines(lesson_list)

    if "complete" in user_decision:
        number = int(input("number of lesson to that are completed: "))

        # getting current list
        with open('lesson_learn.txt', 'r') as file:
            # equal to writeline but just reading
            lesson_list = file.readlines() # list was created here

        lesson_to_remove = lesson_list[number - 1].strip("\n")
        removed = lesson_list.pop(number - 1) # removes the number selected
        with open('lesson_learn.txt','w') as file:
            file.writelines(lesson_list)
        print(f'out of lesson list {lesson_to_remove} was removed')

    if "exit" in user_decision:
        print("Goodbye")
        break
