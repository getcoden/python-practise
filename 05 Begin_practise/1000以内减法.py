import random as ran


r = 0
for i in range(10):
    # 随机出两个数：
    ans = ran.randint(1, 1000)
    res = ran.randint(1, 1000)

    # 比较两个数的大小：
    if ans >= res:
        aaa = ans - res
        bbb = input(str(ans) + "-" + str(res) + "=")
        if bbb == "退出":
            break
        if str(aaa) == bbb:
            print("正确")
            r = r + 10
            print("加10分")
        else:
            print("错误" + str(aaa))
    elif res >= ans:
        aaa = res - ans
        bbb = input(str(res) + "-" + str(ans) + "=")
        if bbb == "退出":
            break
        if str(aaa) == bbb:
            print("正确")
            r = r + 10
            print("加10分")
        else:
            print("错误" + str(aaa))
print("共" + str(r) + "分")
