from utils_gui import get_lesson, write_lesson
import FreeSimpleGUI as sg
#freesimplegui 5.0.0 or above
label = sg.Text("Type in a lesson: ")
input_box = sg.InputText(tooltip="Enter lesson")
button_input = sg.Button("Enter Lesson")
quit_button = sg.Button("Quit")

window = sg.Window("My lessons List",
                   layout=[[label, input_box],[quit_button, button_input]],
                   font=('Helvetica', 15))
window.read()
window.close()