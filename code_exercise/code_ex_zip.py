filenames = ['zip_reports/doc.txt', 'zip_reports/report.txt', 'zip_reports/presentation.txt']
contents = ["Hello", "Hello", "Hello"]

for content, files in zip(contents, filenames):
    file = open(files, 'w')
    file.write(content)
    file.close()

