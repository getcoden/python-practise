# 找素数，利用else

k = 0
for num in range(2, 101):  # 生成从2到89的序列
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print('生成的素数有:{}'.format(num))
        k += 1

print('\n100以内的素数共有{}个'.format(k))
