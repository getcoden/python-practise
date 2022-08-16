import PySimpleGUI as sg


frame_layout = [
    [sg.T('Text inside of a frame')],
    [sg.CB('Check 1'), sg.CB('Check 2')],
]
layout = [
    [sg.Frame('My Frame Title', frame_layout,
              font='Any 12', title_color='blue')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Frame with buttons', layout, font=("Helvetica", 12))

# show it all again and get buttons
event, values = window.read()

while True:
    event, value = window.read()
    if event in (None, 'q'):
        break

window.Close()
