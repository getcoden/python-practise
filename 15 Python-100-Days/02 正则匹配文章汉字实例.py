import re
re_test = r"D:\cblog\python-practise\14 Pyhon100Cases\1.txt"
with open(re_test, 'r', encoding='utf-8') as f:
    ff = f.read()


re_compile = re.compile(r"[\u4e00-\u9fa5]+")
T = re.findall(re_compile, ff)
print(T)
print(type(T))
print(re.split(r'[\s,：。]+', T[0]))

# -*- coding:utf-8 -*-


str = "a23b\na34b"

print(re.findall(r"^a(\d+)b", str))
# 输出['23']

print(re.findall(r"^a(\d+)b", str, re.M))
#输出['23', '34']
