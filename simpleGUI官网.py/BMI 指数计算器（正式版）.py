import PySimpleGUI as sg


# 主题设置
sg.theme('LightBrown4')


def calc_bmi(h, w):
    try:
        h, w = float(h), float(w)
        bmi = round(w / h ** 2, 2)
        if bmi < 18.5:
            standard = '过轻，增加营养哦!'
        elif 18.5 <= bmi <= 23.9:
            standard = '正常，恭喜！'
        elif 24.0 <= bmi <= 27.9:
            standard = '过重,得减肥了！'
        else:
            standard = '肥胖,得减肥了！'
    except (ValueError, ZeroDivisionError):
        return None
    else:
        return f'BMI 值为:{bmi}, {standard} @_@'


# 布局设置
col_layout = [[sg.Text('请输入您的身高(米)   '), sg.InputText('', size=(20, 50), key='-IN1-')],
              [sg.Text('请输入您的体重(千克)'), sg.InputText('', size=(20, 50), key='-IN2-')]]

col_layout1 = [[sg.Text(''), sg.Text(''), sg.Text(''), sg.Button('计算 BMI', key='submit'), sg.Text(''), sg.Text(''),
                sg.Button('清空', key='clear_input'), sg.Text(''), sg.Text(''), sg.Quit('退出', key='q')],
               [sg.Text('')]]

col_layout2 = [[sg.Text(''), sg.Text('')], [sg.Text('', key='bmi', size=(27, 15), font=(
    "微软雅黑", 16), text_color='black')], ]


def clear_input():
    window.FindElement('-IN1-').Update('')
    window.FindElement('-IN2-').Update('')
    return None

# col_layout3 = [[sg.Text('''【正常来说，标准体重就是人体正常的体
# 重与身高比，而这个比值我们简称为 BMI
# 指数，标准体重计算公式又称为 BMI 计
# 算公式，一个健康人的正常 BMI 值范围
# 应该是在：18.5 ～24 之间，而标准体
# 重只是一个相对的概念，并没有一个固定
# 的数值，BMI 是一种相当简陋的健康评估
# 方式，仅供参考。不管我们的 BMI 值或
# 者体重怎么样，我们都应该保持良好的生
# 活以及饮食习惯，毕竟病从口入，多运动
# 才是健康长寿的核心要素。】''', font=(
#     "微软雅黑", 12), text_color='black')], ]


layout = [col_layout, [sg.Text('')], col_layout1, [
    sg.Frame('程序结果输出', col_layout2)], ]


# 创建窗口
window = sg.Window('BMI计算器，制作： 拂晓 6年级(8)班  吴骏琪，指导：张 飞', layout, font='微软雅黑',
                   icon=r"C:\Users\win\Desktop\ccc\f7.ico", size=(720, 450), keep_on_top=True)  # 窗口控制 , resizable=True, finalize=True

# 事件循环
while True:
    event, value = window.read()
    if event == 'submit':
        bmi = calc_bmi(value['-IN1-'], value['-IN2-'])
        if bmi:
            window.FindElement('bmi').Update(bmi, text_color='black')
        else:
            window.FindElement('bmi').Update('输入有误！', text_color='red')

    if event == 'clear_input':
        # window.FindElement('-IN1-').Update('')
        # window.FindElement('-IN2-').Update('')
        clear_input()

    elif event in (None, 'q'):
        break

window.Close()
