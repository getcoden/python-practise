import random
rand_num=random.randint(1,100)
while 1:
#     print('�������%d' %rand_num)
    num = int(input('����������:'))
    if num==rand_num:
        print('�������')
        is_continue=input('�Ƿ�����һ��(yes/no?)')
        if is_continue !='y':
            break
        else:
            rand_num = random.randint(1,100)
    elif num<rand_num:
        print('��С��')
    else:
        print('�´���')
        