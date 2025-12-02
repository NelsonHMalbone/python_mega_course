from apps.utils import get_lesson, write_lesson
import FreeSimpleGUI as sg
#freesimplegui 5.0.0 or above
label = sg.Text("Type in a lesson: ")
input_box = sg.InputText(tooltip="Enter lesson", key="lesson_key")
button_input = sg.Button("Enter")
quit_button = sg.Button("Quit")
edit_button = sg.Button("Edit")
list_box = sg.Listbox(values=get_lesson(),
                      key='lesson_box',
                      enable_events=True,
                      size=[45,10])

window = sg.Window("My lessons List",
                   layout=[[label, input_box],
                           [quit_button, button_input, edit_button],
                           [list_box]],
                   font=('Helvetica', 15))
# prevent program from closing when pushing the enter button

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values["lesson_box"])
    match event:
        case "Enter":
            lesson_list = get_lesson()
            new_lessons = values["lesson_key"] + "\n"
            lesson_list.append(new_lessons)
            write_lesson(lesson_list)

        case "Edit":
            # getting lesson user selected 0 is to get the string
            lesson_to_edit = values["lesson_box"][0] # new lesson
            new_lessons = values['lesson_key'] # lesson to be edited

            # getting current todos
            lessons = get_lesson()
            index = lessons.index(lesson_to_edit)
            lessons[index] = new_lessons
            write_lesson(lessons)

            # to update list box in real time
            window['lesson_box'].update(values=lessons)

        # prevents a error message when closing out app before you get the "quit" button to work
        #case sg.WIN_CLOSED:
            #break

        case "Quit":
            break
window.close()