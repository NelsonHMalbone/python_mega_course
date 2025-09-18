# changing the file names so that txt is at the end of them
# list of file names.
file_name = ["filename_1", "filename_2", "filename_3"]

# what to transform the _ to a - and add a .txt at the end of it

# using list comperhension
file_names = [filename.replace("_", "-") + ".txt" for filename in file_name]

print(file_names)

