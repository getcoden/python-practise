import PySimpleGUI as sg


# 设置主题
sg.theme('TanBlue')


def calc_df(w, h, y):
    try:
        w, h, y = float(w), float(h), float(y)
        day_df = round(w * h * y, 2)
        mon_df = round(w * h * y*31, 2)
        year_df = round(w * h * y*365, 2)

    except (ValueError, ZeroDivisionError):
        return None
    else:
        return day_df, mon_df, year_df


def clear_input():
    window.FindElement('-IN1-').Update('')
    window.FindElement('-IN2-').Update('')
    window.FindElement('-IN3-').Update('')
    return None


frame_1 = [[sg.Text(' '), sg.Text('消耗功率：'), sg.Text(''), sg.Input(
    '', size=(25, 1), key='-IN1-'), sg.T('瓦')],
    [sg.Text('每日使用时数：'), sg.Input('', size=(25, 1), key='-IN2-'), sg.T('小时')],
    [sg.Text(''), sg.Text(''), sg.Text('电价/度：'), sg.Text(''), sg.Input('',
                                                                       size=(25, 1), key='-IN3-'), sg.T('元')], ]

col_1 = [[sg.Button('进行计算', key='submit', button_color='green'), sg.Text(''), sg.Text(''),
          sg.Button('清空', key='clear_input'), sg.Text(''), sg.Text(''), sg.Quit('退出', key='q')],
         [sg.Text('')], ]

frame_2 = [[sg.T(' '), sg.T('每日耗电花费金额：'), sg.T('', key='output1', size=(28, 1), font=("微软雅黑", 10))],
           [sg.Text('')],
           [sg.T(' '), sg.T('每月耗电花费金额：'), sg.T('', key='output2',
                                               size=(28, 1), font=("微软雅黑", 10))],
           [sg.Text('')],
           [sg.T(' '), sg.T('每年耗电花费金额：'), sg.T('', key='output3',
                                               size=(28, 1), font=("微软雅黑", 10))],
           ]

layout = [
    # key 值代表了是这个输入框输入的值，以字典的 键 值来表示，这个用于找到输入框并跟新它的值
    [sg.Frame('', frame_1)],
    [sg.Column(col_1, justification='c')],
    [sg.Frame('计算结果', frame_2)],
]

# 创建窗口，将视窗放在窗口中 ‘天气小助手’为窗口的名字
window = sg.Window('电费小助手，指导：张 飞', layout,
                   font=("微软雅黑", 12))

# 事件循环
while True:
   # 获取输入框和按钮元素的值
    event, value = window.read()
    if event == 'submit':
        df = calc_df(value['-IN1-'], value['-IN2-'], value['-IN3-'])
        if df:
            window.FindElement('output1').Update(day_df, text_color='black')
            window.FindElement('output2').Update(mon_df, text_color='black')
            window.FindElement('output3').Update(year_df, text_color='black')
        else:
            window.FindElement('output1').Update('输入有误！', text_color='red')
            window.FindElement('output2').Update('输入有误！', text_color='red')
            window.FindElement('output3').Update('输入有误！', text_color='red')

    if event == 'clear_input':
        clear_input()

    elif event in (None, 'q'):
        break

window.Close()
