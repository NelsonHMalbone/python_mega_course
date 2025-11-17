# working with data structures, be using json files to build a quilt test
# building a test to have user answer some questions then at the end will show how many answer you got right
# with correct/incorrect, user answer (ex:1), correct/incorrect with answer

import json

with open("bonus_15/questions.json", "r") as content_file:
    content = content_file.read()

data = json.loads(content)
# start with score of 0 after step 4
score = 0

# step 1
# created a nest for loop
for question in data:
    print(question["question_text"])
    # step 2
    for index, alt in enumerate(question["alternatives"]):
        print(index + 1, ":", alt)

    # step 3
    # getting user answer
    # in json file the answer is using intergers
    user_answer = int(input("Enter your answer: "))

    # step 4
    # injecting a new data structure
    question["user_answer"] = user_answer

    # step 5
    # calculating score
    if question["user_answer"] == question["correct_answer"]:
        score = score + 1

# step 6
# show user correct and wrong answers
for index,question in enumerate(data):
    message = (f"{index + 1}: your answer is: {question['user_answer']}, " 
               f"Correct answer {question['correct_answer']}")
    print(message)

print(score, "/", len(data))
