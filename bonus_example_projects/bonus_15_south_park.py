import json

with open("bonus_15/question_south_park.json", "r") as content_file:
    content_data = content_file.read()

data = json.loads(content_data)

# adding a score
score = 0

# asking the questions
for question in data:
    print(question["questions_text"])
    for index, alt in enumerate(question["alternatives"]):
        print(index + 1, ":", alt)
    # allowing the user to choose the answer
    # needs to be a int user is choicing a numbers
    user_choice = int(input("Enter your answer: "))
    # injecting new data structure
    question["user_answers"] = user_choice


for index, question in enumerate(data):
    if question["user_answers"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"

    else:
        result = "Wrong Answer"

    message_return = (f"{index + 1} {result} - Your Answer: {question['user_answers']} "
                      f"Correct answer: {question['correct_answer']}")
    print(message_return)

print(score, "/", len(data))