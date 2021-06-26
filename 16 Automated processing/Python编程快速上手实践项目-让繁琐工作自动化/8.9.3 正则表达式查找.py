#! python3
# this is program named 'Regex Search TXT'

"""
编写一个程序，打开文件夹中所有的.txt 文件，查找匹配用户提供的正则表达
式的所有行。结果应该打印到屏幕上
"""

import re
import os

# 编写一个正则表达式，匹配txt中所有小写5个字母的单词
five_word = re.compile(r'\s[a-z]{5}\s')

# 打开指定文件夹的所有txt文件，匹配所有行
re_ans = []

pathname = r'c:\users\hp\desktop'
for filename in os.listdir(pathname):
    if filename.endswith('.txt'):
        with open(filename, 'r') as f:
            t_text = f.read()
            t_re_find = five_word.findall(t_text)
            re_ans += t_re_find

print(re_ans)

'''
思路：

用了个简单的正则（找5个小写字母的单词）
配合os.listdir，找出txt文件，并for循环一一打开并匹配正则
'''
