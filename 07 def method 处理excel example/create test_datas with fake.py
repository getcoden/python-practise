from faker import Faker
from datetime import date, datetime, timedelta
import pandas as pd
import random
import time

# first, import a similar Provider or use the default one

from faker.providers import BaseProvider

# create new provider class


class MyProvider(BaseProvider):
    def foo(self):
        table = ['五1班', '五2班', '五3班', '五4班']
        return random.choice(table)

    def d(self):
        def t():
            def strTimeProp(start, end, prop, frmt):
                stime = time.mktime(time.strptime(start, frmt))
                etime = time.mktime(time.strptime(end, frmt))
                ptime = stime + prop * (etime - stime)
                return int(ptime)

            def randomDate(start, end, frmt='%Y-%m-%d %H:%M:%S'):
                return time.strftime(frmt, time.localtime(strTimeProp(start, end, random.random(), frmt)))
            start = '2009-08-02 00:00:00'
            end = '2013-11-01 00:00:00'
            lenth = 10
            return randomDate(start, end)
        return t()


# then add new provider to faker instance
# fake.add_provider(MyProvider)
# now you can use:
# print(fake.foo())
fake = Faker('zh_CN')


class PtDataGen:
    def __init__(self):
        self.data_dict = {}

    def fake_data(self):
        fake.add_provider(MyProvider)
        pt_profile = fake.profile()
        self.data_dict['序号'] = f"{fake.pyint(1,350):03}"
        self.data_dict['学籍号'] = f"{fake.pyint(15000,17000):05}"
        self.data_dict['班级'] = fake.foo()
        self.data_dict['姓名'] = pt_profile['name']
        self.data_dict['年龄'] = fake.pyint(9, 13)
        self.data_dict['性别'] = pt_profile['sex']
        self.data_dict['出生日期'] = fake.d()
        self.data_dict['语文'] = fake.pyint(0, 100)
        self.data_dict['数学'] = fake.pyint(0, 100)
        self.data_dict['英语'] = fake.pyint(0, 100)
        self.data_dict['电话'] = fake.phone_number()
        self.data_dict['邮箱'] = fake.email()
        self.data_dict['地址'] = fake.address()

    def get_data_series(self):
        return pd.Series(self.data_dict)

    def get_data_dict(self):
        return self.data_dict

# 生成数据的数量


rst_list = []
for _ in range(100):
    pt_data = PtDataGen()
    pt_data.fake_data()
    rst_list.append(pt_data.get_data_dict())

df_pt_list = pd.DataFrame(rst_list)

# 保存生成的数据

df_pt_list.to_excel('./测试成绩表.xlsx', index=False)
