contents = ['Bonus 6 text 1', 'Bonus 6 text 2', 'Bonus 6 text 3']

filenames = ['bonus_6_file.txt', 'bonus_6_file2.txt', 'bonus_6_file3.txt']

for content, file in zip(contents, filenames):
    files = open(file, 'w')
    files.write(content)