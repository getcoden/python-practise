def healthe(m):
    if m=="Y"or 'y':
        print("欢迎，请进入游戏！")
        age=input("你今年多大了？\n")
        if 0<int(age)<12:
            print("由于你年龄偏小，所以只能玩一个小时哦！")
        elif 12<=int(age)<18:
            print("由于你接近成年但未成年，所以你可以玩俩小时哦！")
        elif 18<=int(age)<150:
            print("你已经是成年人了，请控制好游戏时间哦！")
        else:
            print("别闹，你输入的不是人的年龄！！！")
    elif m=="N"or 'n':
        print("想什么呢？快回去写作业去！！！")
    else:
        print("请不要答非所问可好？")
con=input("请问作业做完了吗？\n")
print(healthe(con))