import re

# 正则获取目标信息


def get_re_str(str):
    res = re.findall(
        r'^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', str)
    return res

# 读取目标文本文件


def get_str(path):
    f = open(path, encoding="utf-8")
    data = f.read()
    f.close()
    return data

# 保存得到的信息


def save_res(res, save_path):
    save_file = open(save_path, 'w')
    for phone in res:
        save_file.write(phone)
        save_file.write('\n')
    save_file.close()
    print('信息读取OK，信息共计：'+str(len(res)))


path = input("请输入文件路径：")
save_path = input("请输入文件保存路径：")
# read_str=get_str(path)
res = get_re_str(get_str(path))
save_res(res, save_path)
