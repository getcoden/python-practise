# 方法一
def fac():
    num = int(input("请输入一个数字："))
    factorial = 1
    # 查看数字是负数，0或者正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        for i in range(1, num+1):
            factorial = factorial*i
        print("%d的阶乘为%d" % (num, factorial))


if __name__ == '__main__':
    fac()
    
# 方法二


def fac():
    num = int(input("请输入一个数字："))
    # 查看数字是负数，0或者正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        print("%d的阶乘为%d" % (num, factorial(num)))


def factorial(n):
    result = n
    for i in range(1, n):
        result = result*i
    return result


if __name__ == '__main__':
    fac()


# 方法三
def fac():
    num = int(input("请输入一个数字："))
    # 查看数字是负数，0或者正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        print("%d的阶乘为%d" % (num, fact(num)))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    fac()
