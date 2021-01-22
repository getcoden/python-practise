def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n = int(input('>>>:'))
a = fact(n)
print(f'你输入的是{n},它的阶乘为{a}')
