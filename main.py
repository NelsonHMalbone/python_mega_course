print("Lessons Learn Tracker")

#print("Enter your lesson Learned:")
prompt_user_text = "Enter your lesson Learned: " # variable to store message
user_text = input(prompt_user_text)

# adding more inputs
user_text2 = input(prompt_user_text)
user_text3 = input(prompt_user_text)

#print("Add a quick note (optional): ")
# no prompt to store message
optional_note = input("Add a quick note (optional): ")

lessons = [user_text, user_text2, user_text3]

print(lessons)
#print(user_text)
#print(optional_note)