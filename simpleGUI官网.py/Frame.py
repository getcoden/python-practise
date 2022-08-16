import PySimpleGUI as sg

left_col = [[sg.Text('Folder'), sg.In(size=(25, 1), key='-FOLDER-'), sg.FolderBrowse()],
            [sg.Listbox(values=[], enable_events=True,
                        size=(40, 20), key='-FILE LIST-')]
            ]

images_col = [[sg.Text('You choose from the list:')],
              [sg.Text(size=(40, 1), key='-TOUT-')],
              [sg.Image(key='-IMAGE-')],
              ]

layout = [[sg.Column(left_col), sg.VSeparator(), sg.Column(images_col)]]

window = sg.Window('Image Viewer', layout, keep_on_top=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    if event == '':
        folder = values['-FOLDER-']
        try:
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [f for f in file_list if os.path.isfile(os.path.join(
            folder, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp'))]
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':
        try:
            filename = os.path.join(
                values['-FOLDER-'], values['-FILE LIST-'][0])
            window['-TOUT-'].update(filename)
            window['-IMAGE-'].update(filename=filename)
        except:
            pass

window.close()
