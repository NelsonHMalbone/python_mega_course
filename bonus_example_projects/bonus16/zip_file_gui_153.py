# 11-22 making the gui of the file zipper

import FreeSimpleGUI as sg

text_1 = sg.Text("Select files to compress: ")
text_2 = sg.Text("Select destination folder: ")
input_1 = sg.Input()
input_2 = sg.Input()
file_selector_1 = sg.FilesBrowse("Choose")
file_selector_2 = sg.FilesBrowse("Choose")
compress_btn = sg.Button("Compress")


main_window = sg.Window("File Zipper", layout=[[text_1,input_1 ,file_selector_1],
                                               [text_2, input_2, file_selector_2],
                                               [compress_btn]])
main_window.read()
main_window.close()