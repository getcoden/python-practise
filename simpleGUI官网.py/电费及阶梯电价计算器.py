# def calc_df(w, h, y):
#     try:
#         w, h, y = float(w), float(h), float(y)
#         day_df = round((w/1000) * h * y, 2)
#         mon_df = round((w/1000) * h * y*31, 2)
#         year_df = round((w/1000) * h * y*365, 2)

#     except (ValueError, ZeroDivisionError):
#         return None
#     else:
#         return day_df, mon_df, year_df


# print(calc_df(200, 10, 0.56))


'''

def df_calc():
    sum_df = float(tc)
    if sum_df <= 100:
        fei_yong = sum_df * 0.56
        prfloat('本月电费正常为：' + str(fei_yong))
    else:
        chao_liang = sum_df * 0.56+(sum_df - 100) * (0.56 * 0.56 * 0.2)
        prfloat('本月电费超标：'+str(chao_liang))


while 1:
    tc = input('输入本月用电量( q 退出):')
    if tc == 'q':
        break
    else:
        df_calc()
'''

"""


某电价规定：月用电量在 150 千瓦时及以下部分按每千瓦时 0.4463 元收费，月用电量在 151~400 千瓦时的部分按每千瓦时 0.4663 元收费，月用电量在 401 千瓦时及以上部分按每千瓦时 0.5663 元收费。 请编写一个程序，根据输入的月用电量（单位以千瓦时计），按该电价规定计算出应缴的电费（单位以元计）。

输入格式:
首先输入一个正整数 T，表示测试数据的组数，然后是 T 组测试数据。对于每组测试，输入一个整数 n（0≤n≤10000），表示月用电量。

输出格式:
对于每组测试，输出一行，包含一个实数，表示应缴的电费。结果保留 2 位小数。

    """

'''


import math
x = float(input('测试数据的组数:'))
for i in range(0, x):
    n = float(input('每月用电量:'))
    if n <= 150:
        t = n*0.4463
    elif 151 <= n <= 400:
        t = 150*0.4463+(n-150)*0.4663
    else:
        t = 150*0.4463+250*0.4663+(n-400)*0.5663
    print("{0:.2f}".format(t))
'''

'''
def calc_df(w, h, y):
    try:
        w, h, y = float(w), float(h), float(y)
        day_df = round((w/1000) * h * y, 2)
        mon_df = round((w/1000) * h * y*31, 2)
        year_df = round((w/1000) * h * y*365, 2)

    except (ValueError, ZeroDivisionError):
        return None
    else:
        return day_df, mon_df, year_df

dd = calc_df(200, 10, 0.56)
print(dd[2])
'''
