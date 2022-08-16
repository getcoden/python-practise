import PySimpleGUI as sg

"""
layout = [[sg.T('文件名'), sg.In(), sg.FileBrowse('浏览')],
          [sg.OK('确定'), sg.Cancel('取消')]]

window = sg.Window('获取文件案例', layout)

event, values = window.read()

print(event, values)

text_input = values[0]
sg.popup('You entered', text_input)
window.close()
"""
# If you want to use a key instead of an auto-generated key:

"""
layout = [[sg.T('文件名1'), sg.In(key='-IN-'), sg.FileBrowse('浏览')],
          [sg.T('文件名2'), sg.In(key='-IN2-'), sg.FileBrowse('浏览2')],
          [sg.OK('确定'), sg.Cancel('取消')]]

window = sg.Window('获取文件案例', layout)


while True:
    event, values = window.read()
    print(event, values)
    if event in (None, '取消'):
        break
    text_input = values['-IN-']
    text_input1 = values['-IN2-']

    sg.popup('You entered', text_input, text_input1)

window.close()

"""
# Recipe - Pattern 2B - Persistent window (multiple reads using an event loop + updates data in window)

"""
sg.theme('BluePurple')

layout = [[sg.Text('You typed chars appear here:'), sg.Text(size=[15, 1], key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')],
          ]
window = sg.Window('Pattern 2B', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])


window.close()
"""

"""

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Some text on Row 1'), sg.InputText('', key='-IN-')],
          [sg.Text('Enter something on Row 2'), sg.InputText('bbb')],
          [sg.Text('', key='-OUTPUT-', size=(30, 2))],
          [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break

    if event == 'OK':
        window.Element['-OUTPUT-'].update(values['-IN-'])
    # print('You entered ', values)

window.close()
"""

layout = [[sg.Text('You entered text:'), sg.Input(key='-IN-'), sg.Multiline(size=(25, 10), key='-OUTPUT-')],
          #   [sg.Push(), sg.Text(size=(20, 2), key='-OUTPUT-'), sg.Push()],
          [sg.Push(), sg.Button('Show'), sg.Button('Exit'), sg.Push()]]

window = sg.Window('OUTPUT UPDATE', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if event == 'Show':
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
