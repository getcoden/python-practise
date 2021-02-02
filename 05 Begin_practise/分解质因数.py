# 分解质因数

def zhishu(n):
    x = True
    for i in range(2, n):
        if n % i == 0:
            x = False
            break
    return x


def fenjie():
    n = int(input("enter a number:"))
    m = n
    line = []
    i = 2
    while True:
        if not zhishu(n):
            if n % i == 0:
                line.append(i)
                n = n//i
            else:
                i += 1
        else:
            s = n
            break
    print(str(m)+"=", end="")
    for j in line:
        print(j, end="*")
    print(s)


fenjie()
