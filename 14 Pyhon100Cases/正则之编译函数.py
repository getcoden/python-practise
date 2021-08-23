
"""
python 之 re.compile 的使用

compile 函数用于编译正则表达式，返回一个正则表达式对象，供 match ()、search () 、findall () 等函数使用。
格式：re.compile (正则表达式【, 标志位】)

    """


import re

'''
def main():
    content = 'Hello, I am Jerry, from Chongqing, a montain city, nice to meet you……'
    # \w* 表示匹配由大小写英文字母数字和下划线组成的 0 个或多个字符 o 表示匹配字符 o \w*o\w* 表示匹配含有 o 的字符串 (不管 o 在首字母还是在尾字母还是在中间)
    regex = re.compile('\w*a\w*')
    x = regex.findall(content)
    print(x)


if __name__ == '__main__':
    main()
# ['Hello', 'from', 'Chongqing', 'montain', 'to', 'you']
'''


def main():
    content = 'af 张飞ad f545fy5a 飞1厅飞s2359'
    # \w* 表示匹配由大小写英文字母数字和下划线组成的 0 个或多个字符 o 表示匹配字符 o \w*o\w* 表示匹配含有 o 的字符串 (不管 o 在首字母还是在尾字母还是在中间)
    regex = re.compile(r"[\u4e00-\u9fa5]+")
    x = regex.findall(content)
    print(x)


if __name__ == '__main__':
    main()
# ['Hello', 'from', 'Chongqing', 'montain', 'to', 'you']
