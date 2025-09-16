
filenames = ["multiple_files_exercise(67)/a.txt",
             "multiple_files_exercise(67)/b.txt",
             "multiple_files_exercise(67)/c.txt"]


for file in filenames:
    with open(file, "r") as f:
        content = f.read()

    print(content)
