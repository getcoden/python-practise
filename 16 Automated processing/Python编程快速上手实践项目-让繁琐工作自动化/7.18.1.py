'''
7.18.1 实践项目：强口令检测
写一个函数，它使用正则表达式，确保传入的口令字符串是强口令。强口令的定义是：
长度不少于8个字符，同时包含大写和小写字符，至少有一位数字。
你可能需要用多个正则表达式来测试该字符串，以保证它的强度。
'''
import re
import pyperclip

len_re = re.compile(r'.{8,}')
a_re = re.compile(r'[a-z].*[A-Z]|[A-Z].*[a-z]')
num_re = re.compile(r'\d')


def password_test(password):
    if len_re.search(password) and a_re.search(password) and num_re.search(password):
        print('your password is strong enough!')
    else:
        print('please reset your password')


password = str(pyperclip.paste())
password_test(password)
