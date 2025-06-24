print("Lessons Learn Tracker")

#print("Enter your lesson Learned:")
prompt_user_text = "Enter your lesson Learned: " # variable to store message

# list method
lesson_list = []

while True:
    user_text = input(prompt_user_text)
    # optional_note = input("Add a quick note (optional): ")
    lesson_list.append(user_text)
