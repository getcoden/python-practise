import PySimpleGUI as sg
# import PySimpleGUIQt as sg
import os.path
import PIL.Image
import io
import base64
"""
col_layout = [[sg.T('Name'), sg.In()],
              [sg.T('Address'), sg.In()]]


laylout = [[sg.Listbox(list(range(10)), size=(10, 5), key='-LBOX-'), sg.Column(col_layout)],
           [sg.Button('Go'), sg.Button('Exit')]]


window = sg.Window('Window Title', laylout,
                   auto_size_text=False, default_element_size=(12, 1), keep_on_top=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

window.close()
    """


# Frame


col_layout = [[sg.T('Name'), sg.In()],
              [sg.T('Address'), sg.In()]]

col_layout2 = [[sg.T('Name'), sg.In()],
               [sg.T('Address'), sg.In()]]

col_layout3 = [[sg.T('Name'), sg.In()],
               [sg.T('Address'), sg.In()]]

col_layout4 = [[sg.T('Name'), sg.In()],
               [sg.T('Address'), sg.In()]]

"""
laylout = [[sg.Listbox(list(range(10)), size=(10, 5), key='-LBOX-')],
           [sg.Pane([sg.Col(col_layout3), sg.Col(col_layout2)])],
           #    [sg.TabGroup([[sg.Tab('Tab 1', col_layout), sg.Tab('2', col_layout2), sg.Tab(
           #        '3', col_layout3), sg.Tab('Tab4', col_layout4)]])],

           [sg.Button('Go'), sg.Button('Exit')]]


window = sg.Window('Window Title', laylout,
                   auto_size_text=False, default_element_size=(15, 2), keep_on_top=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break

window.close()
"""


# First the window layout ....2 columns
"""
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
"""


# First the window layout...2 columns

left_col = [[sg.Text('Folder'), sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'), sg.FolderBrowse()],
            [sg.Listbox(values=[], enable_events=True,
                        size=(40, 20), key='-FILE LIST-')],
            [sg.Text('Resize to'), sg.In(key='-W-', size=(5, 1)), sg.In(key='-H-', size=(5, 1))]]

# For now will only show the name of the file that was chosen
images_col = [[sg.Text('You choose from the list:')],
              [sg.Text(size=(40, 1), key='-TOUT-')],
              [sg.Image(key='-IMAGE-')]]

# ----- Full layout -----
layout = [[sg.Column(left_col, element_justification='c'), sg.VSeperator(
), sg.Column(images_col, element_justification='c')]]

# --------------------------------- Create Window ---------------------------------
window = sg.Window('Multiple Format Image Viewer', layout, resizable=True)

# ----- Run the Event Loop -----
# --------------------------------- Event Loop ---------------------------------
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == '-FOLDER-':                         # Folder name was filled in, make a list of files in the folder
        folder = values['-FOLDER-']
        try:
            # get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []
        fnames = [f for f in file_list if os.path.isfile(
            os.path.join(folder, f)) and f.lower().endswith((".png", ".jpg", "jpeg", ".tiff", ".bmp"))]
        window['-FILE LIST-'].update(fnames)
    elif event == '-FILE LIST-':    # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values['-FOLDER-'], values['-FILE LIST-'][0])
            window['-TOUT-'].update(filename)
            if values['-W-'] and values['-H-']:
                new_size = int(values['-W-']), int(values['-H-'])
            else:
                new_size = None
            window['-IMAGE-'].update(data=convert_to_bytes(filename,
                                                           resize=new_size))
        except Exception as E:
            print(f'** Error {E} **')
            pass        # something weird happened making the full filename
# --------------------------------- Close & Exit ---------------------------------
window.close()
