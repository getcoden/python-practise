import PySimpleGUI as sg


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


# 主题设置
sg.theme('LightBrown4')

# 布局设置
layout = [[sg.Text('请输入您的身高(米)   '), sg.InputText(size=(20, 50))],
          [sg.Text('请输入您的体重(千克)'), sg.InputText(size=(20, 50))],
          [sg.Text('')],
          [sg.Text(''), sg.Text(''), sg.Text(''), sg.Button('计算 BMI', key='submit'), sg.Text(''), sg.Text(''),
           sg.Quit('退出', key='q')],
          [sg.Text('')],
          [sg.Text('程序结果输出:')],
          [sg.Text('', key='bmi', size=(30, 2))],
          [sg.Text('')],
          [sg.Text('BMI 解释:', font=("微软雅黑", 12))],
          [sg.Text('''【正常来说，标准体重就是人体正常的体重与身高比，而这个比值我们简称为 BMI 指数，标准
体重计算公式又称为 BMI 计算公式，一个健康人的正常 BMI 值范围应该是在：18.5 ～24 之间，
而标准体重只是一个相对的概念，并没有一个固定的数值，BMI 是一种相当简陋的健康评估方式，
仅供参考。不管我们的 BMI 值或者体重怎么样，我们都应该保持良好的生活以及饮食习惯，毕竟
病从口入，多运动才是健康长寿的核心要素。】''', font=(
              "微软雅黑", 12), text_color='black')],
          ]

# 创建窗口
window = sg.Window('BMI计算器，制作： 拂晓 6年级(8)班  吴骏琪，指导：张 飞', layout, font='微软雅黑',
                   icon=r"C:\Users\win\Desktop\ccc\f7.ico", size=(720, 450))  # 窗口控制 , resizable=True, finalize=True

# 事件循环
while True:
    event, value = window.Read()
    if event == 'submit':
        bmi = calc_bmi(value[0], value[1])
        if bmi:
            window.Element('bmi').Update(bmi, text_color='black')
        else:
            window.Element('bmi').Update('输入有误！', text_color='red')

    elif event in (None, 'q'):
        break


window.Close()
