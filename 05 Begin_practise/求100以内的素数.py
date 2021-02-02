# 求100以内的素数

num = 1
while num <= 100:
    flag = 0
    a = 2
    while a <= num/2:
        if num % a == 0:
            flag = 1
        a = a + 1
    if flag == 0:
        print(num)
    num = num + 1
