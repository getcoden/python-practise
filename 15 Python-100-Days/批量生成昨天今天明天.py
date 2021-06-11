# from datetime import date, timedelta

# for _i in range(10):
#     yesterday = (date.today() + timedelta(days=-1)).strftime("%Y-%m-%d")
#     print(yesterday)
#     today = date.today()
#     print(today)
#     tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
#     print(tomorrow)

'''
python 获取指定时间段内的随机不重复时间点的实现代码
场景 1：取 N 个 07:30:00-09:30:33 之间的随机时间。
下面是我的代码：
'''
# 2016-12-10 7:06:29 codegay
import random
import datetime

st = "07:30:00"
et = "09:30:33"


def time2seconds(t):
    h, m, s = t.strip().split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def seconds2time(sec):
    m, s = pmod(sec, 60)
    h, m = pmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


sts = time2seconds(st)  # sts==27000
ets = time2seconds(et)  # ets==34233
rt = random.sample(range(sts, ets), 10)
#rt == [28931, 29977, 33207, 33082, 31174, 30200, 27458, 27434, 33367, 30450]
rt.sort()  # 对时间从小到大排序
for r in rt:
    print(seconds2time(r))
