'''
编写一个函数，它以一个列表值作为参数，返回一个字符串。
该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and。
'''


def list2str(alist):
    print(alist)
    a = alist.pop()
    a = 'and ' + a
    alist.append(a)
    b = ', '.join(alist)
    print(b)    # print改成return就可以返回结果


a = ['cat', 'dog', 'cow']

list2str(a)
