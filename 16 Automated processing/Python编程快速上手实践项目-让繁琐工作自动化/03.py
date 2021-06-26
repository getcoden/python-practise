'''3.11.1 Collatz 序列
项目要求：编写一个名为collatz()的函数，它有一个名为number的参数。
如果参数是偶数，那么collatz()就打印出number//2，并返回该值。如果number是奇数，
collatz()就打印并返回3*number+1。然后编写一个程序，让用户输入一个整数，并不断对这个数调用collatz()，直到函数返回值１

'''


def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num == 1:
        return num
    elif num % 2 == 1:
        return num * 3 + 1


try:
    a = int(input('Please input a num: \n'))
    while True:
        a = collatz(a)
        print(a)
        if a == 1:
            break
except ValueError:
    print('Please input a right int num')

'''
项目要求：在前面的项目中添加try和except语句，检测用户是否输入了一个非整数的字符串。
正常情况下，int()函数在传入一个非整数字符串时，会产生ValueError错误，比如int('puppy')。
在except子句中，向用户输出一条信息，告诉他们必须输入一个整数。

'''
try:
    input_int = input('Please input an int: ')
    a = int(input_int)
except ValueError:
    print('Please input an int, not str or float.')
