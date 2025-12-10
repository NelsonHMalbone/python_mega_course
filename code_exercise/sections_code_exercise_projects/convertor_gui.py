import FreeSimpleGUI as sg

feet_text = sg.Text("Enter feet:")
inches_text = sg.Text("Enter inches:")
feet_input_box = sg.InputText(key="feet")
inches_input_box = sg.InputText(key="inches")
convert_btn = sg.Button("Convert")
conversion_lbl = sg.Text("",key="output")

main_window = sg.Window("Convertor",
                        layout=[[feet_text, feet_input_box],
                                [inches_text, inches_input_box],
                                [convert_btn, conversion_lbl]])

"""
What i had was wrong but i did use chatgpt to help me understand where i went wrong

feet_conversion = int(feet_input_box * 0.3048)
inches_conversion = int(inches_input_box * 0.0254)

because the input boxes are a gui element and not a number is was erroring out 
"""


while True:
    event, values = main_window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Convert":
        # user input
        feet_conversion = float(values["feet"])
        inches_conversion = float(values["inches"])

        # convert to meters
        meters = feet_conversion * 0.3048 + inches_conversion * 0.0254

        # output the results
        main_window["output"].update(value=f"Conversion {meters} m")



main_window.close()