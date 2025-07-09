filenames = ['1.Raw Data.txt', '2.Reports.txt', '3.Presentations.txt']

for filename in filenames:
    filename = filename.replace(".", "-", 1)
    # over writing old str with new string with the replacements
    # the 1 tells python to change the first occurace of the . to the -
    print(filename)