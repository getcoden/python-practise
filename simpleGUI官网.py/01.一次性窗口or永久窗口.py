import PySimpleGUI as sg

# layout = [[sg.Text('My one-shot window.')],
#           [sg.InputText()],
#           [sg.Submit(), sg.Cancel()]
#           ]
# window = sg.Window('Window Title', layout)

# event, values = window.read()
# window.close()
# text_input = values[0]
# sg.popup('You entered', text_input)

# ----------------------------------

# layout = [[sg.Text('My one-shot window.')],
#           [sg.InputText(key='-IN-')],
#           [sg.Submit(), sg.Cancel()]]

# window = sg.Window('Window Title', layout)

# event, values = window.read()
# window.close()

# text_input = values['-IN-']
# sg.popup('You entered', text_input)

# ----------------------------------
# event, values = sg.Window('Login Window',
#                           [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
#                            [sg.B('OK'), sg.B('Cancle')]]).read(close=True)

# login_id = values['-ID-']


# ---------------------------------- 永久窗口

sg.theme('DarkAmber')

layout = [[sg.Text('Persistent window')],
          [sg.Input(key='-IN-')],
          [sg.Button('Read'), sg.Exit()]

          ]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
