import FreeSimpleGUI as sg

feet_text = sg.Text("Enter feet:")
inches_text = sg.Text("Enter inches:")
feet_input_box = sg.InputText()
inches_input_box = sg.InputText()
convert_btn = sg.Button("Convert")

main_window = sg.Window("Convertor",
                        layout=[[feet_text, feet_input_box],
                                [inches_text, inches_input_box],
                                [convert_btn]])

main_window.read()
main_window.close()