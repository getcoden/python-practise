from aip import AipOcr  # 导入AipOcr模块，用于做文字识别
import glob
import os

# 人工智能大法好，使用百度 api 批量识别图片上的文字：
# 这是是批量识别，统统放进一个文件夹就 OK 啦～

APP_ID = '27777886'
API_KEY = '4VYr2B9k5rvvOCVHYpzVaQsg'
SECRET_KEY = 'IFaIhSkWXUqq8iElNNfg9Pi1KATYfiCT'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


for root, dirs, files in os.walk(r"D:\1jieya\image", topdown=False):
    for name in files:
        if 'jpg' in name: # 注意图片的扩展名，如果不正确就不能识别出来文字
            filePath = os.path.join(root, name)
            options = {
                'detect_direction': 'true',
                'language_type': 'CHN_ENG',
            }
            with open('C:/Users/win/Desktop/Pic2txt.txt', 'a') as f:
                result = client.basicAccurate(get_file_content(filePath), options)
                # print(result)
                for i in result['words_result']:
                    f.write('\n' + i['words'] + '\n')
                # print(i)
    os.startfile(r'C:/Users/win/Desktop/Pic2txt.txt')  # 自动打开生成的 txt 文件
    # print(i['words'])
