with open("story.txt", 'r') as file:
    content = file.readlines()

with open('story_copy.txt', 'w') as file:
    file.writelines(content)