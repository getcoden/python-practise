
from aip import AipOcr  # 导入AipOcr模块，用于做文字识别
import glob
import os

# 人工智能大法好，使用百度 api 批量识别图片上的文字：
# 这是是批量识别，统统放进一个文件夹就 OK 啦～

APP_ID = '27777886'
API_KEY = '4VYr2B9k5rvvOCVHYpzVaQsg'
SECRET_KEY = 'IFaIhSkWXUqq8iElNNfg9Pi1KATYfiCT'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


path = r"D:\1jieya\image"
files = glob.glob(path+"*.jpg")

txt_file = open('Pic2txt.txt', 'a')


with open(r"D:\1jieya\image\1.jpg", 'rb') as f:

    image = f.read()

    text = client.basicAccurate(image)

# print(text)

n = text['words_result_num']
for i in range(int(n)):
    print(text['words_result'][i]['words'], end='')
