while True:
    shifu = str(input('是否继续选择计算？(Y或者N):'))
    if shifu == 'y':
        pass
    else:
        break
    age = int(input('请输入年龄:'))
    sex = str(input('请输入性别:man或者woman:'))
    if (sex == 'man') or (sex == 'woman'):
        if (age >= 22 and sex == 'man') or (age >= 20 and sex == 'woman'):
            print('可以结婚')
        else:
            print('不可以结婚')
    else:
        print('你输入的性别有误，请重新输入')
        continue
