import random
rand_num=random.randint(1,100)
while 1:
#     print('随机数是%d' %rand_num)
    num = int(input('请输入数字:'))
    if num==rand_num:
        print('你真棒！')
        is_continue=input('是否再来一盘(yes/no?)')
        if is_continue !='y':
            break
        else:
            rand_num = random.randint(1,100)
    elif num<rand_num:
        print('猜小了')
    else:
        print('猜大了')
        