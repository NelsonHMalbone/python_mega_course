from apps.utils import get_lesson, write_lesson
import FreeSimpleGUI as sg
#freesimplegui 5.0.0 or above
label = sg.Text("Type in a lesson: ")
input_box = sg.InputText(tooltip="Enter lesson", key="lesson_key")
button_input = sg.Button("Enter")
quit_button = sg.Button("Quit")
edit_button = sg.Button("Edit")

window = sg.Window("My lessons List",
                   layout=[[label, input_box],[quit_button, button_input, edit_button]],
                   font=('Helvetica', 15))
# prevent program from closing when pushing the enter button

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Enter":
            lesson_list = get_lesson()
            new_lessons = values["lesson_key"] + "\n"
            lesson_list.append(new_lessons)
            write_lesson(lesson_list)

        # prevents a error message when closing out app before you get the "quit" button to work
        #case sg.WIN_CLOSED:
            #break

        case "Quit":
            break
window.close()