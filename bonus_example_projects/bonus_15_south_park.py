import json

with open("bonus_15/question_south_park.json", "r") as content_file:
    content = content_file.read()

data = json.loads(content)

# asking the questions
for question in data:
    print(question["questions_text"])
    for index, alt in enumerate(question["alternatives"]):
        print(index + 1, ":", alt)