import PySimpleGUI as sg

sg.change_look_and_feel('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout2 = [  [sg.Text('My Lord,')],
            [sg.Text('What is your summoner name?'), sg.InputText()],
            [sg.Text('Are your a human?'), sg.Radio('I am a human!     ', "RADIO1"), sg.Radio('I am a ROBOT!    ', "RADIO1", default=True)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Introduce yourself!', layout2)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    robot_statut = "as an IA!"
    if values[1] == True:
        robot_statut = "as a humanoid!"
    print(values[0], "has joined the game", robot_statut)
    break

window.close()