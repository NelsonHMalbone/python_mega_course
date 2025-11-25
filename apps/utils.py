FILEPATH = "lesson_learn.txt" # for gui
# FILEPATH = "apps/lesson_learn.txt" # for cli

def get_lesson(filepath=FILEPATH):
    """read a text file i n return the
    list of lesson items
    """
    # will use the filepath that is show in add,show, and edit
    with open(filepath, 'r') as file_local:
        # equal to writeline but just reading
        lesson_list_local = file_local.readlines()  # list was created here
    return lesson_list_local

# to write to files
# does not need a variable to be called unlike the get lesson
def write_lesson(lesson_arg, filepath=FILEPATH):
    """write a lesson item list in the text file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(lesson_arg)

if __name__ == "__main__":
    print()
