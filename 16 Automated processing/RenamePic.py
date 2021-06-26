def get_jpg():
    jpgs = []
    path = "F:\p"
    for i in os.listdir(path):  # 获取文件列表
        if i.split(".")[-1] == "png":  # 筛选jpg文件（截图）
            oldname = os.path.join(path, i)  # 旧文件名
            i = i.replace('微信截图_', '')
            newname = os.path.join(path, i)  # 新文件名
            os.rename(oldname, newname)  # 改名
            jpgs.append(i)
    return jpgs
# print(get_jpg())
