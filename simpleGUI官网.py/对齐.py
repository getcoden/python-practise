import PySimpleGUI as sg
from tkinter import *
sg.theme('DarkAmber')
layout = [
    [sg.Text('Enter the value', justification='center')],
    [sg.Input(justification='center')],
    [sg.Button('Enter', 'center')]
]

window = sg.Window('My new window', layout,
                   element_justification='c')

while True:
   # Read the event that happened and the values dictionary
    event, values = window.read()
    print(event, values)
    # If user closed window with X or if user clicked "Exit" button then exit
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Button':
        print('You pressed the button')
window.close()
