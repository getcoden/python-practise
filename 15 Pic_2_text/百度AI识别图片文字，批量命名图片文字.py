# 识别图片文字，批量命名图片文字

import os
from aip import AipOcr
import re
import datetime

# 新建一个AipOcr对象
config = {
    'appId': '24608598',
    'apiKey': 'kAHxRGWszGl95maX0GgIKpGC',
    'secretKey': 'NA1or974XAPSCgo7SlmMoYBzzZKhgoGM'
}
client = AipOcr(**config)

pic_dir = r"C:\Users\win\Desktop\1"


# 读取图片
def get_file_content(file_path):
    with open(file_path, 'rb') as fp:
        return fp.read()


# 识别图片里的文字
def img_to_str(image_path):
    image = get_file_content(image_path)
    # 调用通用文字识别, 图片参数为本地图片
    result = client.basicGeneral(image)
    # 结果拼接返回
    words_list = []
    if 'words_result' in result:
        if len(result['words_result']) > 0:
            for w in result['words_result']:
                words_list.append(w['words'])
            file_name = get_longest_str(words_list)
            print(file_name)
            file_dir_name = pic_dir + str(file_name).replace("/", "") + '.jpg'
            if os.path.exists(file_dir_name):  # 处理文件重名问题
                sec = datetime.datetime.now().microsecond  # 获取当前毫秒时值
                file_dir_name = pic_dir + \
                    str(file_name).replace("/", "") + str(sec) + '.jpg'
            try:
                os.rename(image_path, file_dir_name)
            except Exception:
                print(" 重命名失败：", image_path, " => ", file_name)


# 获取字符串列表中最长的字符串
def get_longest_str(str_list):
    pat = re.compile(r'[\u4e00-\u9fa5A-Za-z]+')
    str = max(str_list, key=hanzi_len)
    result = pat.findall(str)
    return ''.join(result)


def hanzi_len(item):
    pat = re.compile(r'[\u4e00-\u9fa5]+')
    sum = 0
    for i in item:
        if pat.search(i):
            sum += 1
    return sum


# 遍历某个文件夹下所有图片
def query_picture(dir_path):
    pic_path_list = []
    for filename in os.listdir(dir_path):
        pic_path_list.append(os.path.join(dir_path, filename))
    return pic_path_list


if __name__ == '__main__':
    pic_list = query_picture(pic_dir)
    if len(pic_list) > 0:
        for i in pic_list:
            img_to_str(i)
