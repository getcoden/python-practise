from aip import AipOcr  # 导入AipOcr模块，用于做文字识别
import os


# 人工智能大法好，使用百度 api 批量识别图片上的文字：
# 这是是批量识别，统统放进一个文件夹就 OK 啦～

APP_ID = '27777886'
API_KEY = '4VYr2B9k5rvvOCVHYpzVaQsg'
SECRET_KEY = 'IFaIhSkWXUqq8iElNNfg9Pi1KATYfiCT'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


path = r"D:\1jieya\image"
path_list = os.listdir(path)
path_list.sort(key=lambda x: int(x.replace("images_", "").split('.')[0]))
# path_list.sort(key=lambda x: int(x.split('.')[0]))
print('图片文件为:' + str(path_list) + '\n')
print('正在上传图片进行文字识别输出......')
for filename in path_list:
    if 'jpg' in filename:
        filePath = os.path.join(path, filename)
        options = {
            'detect_direction': 'true',
            'language_type': 'CHN_ENG',
        }
        with open('C:/Users/win/Desktop/Pic2txt.txt', 'a') as f:
            result = aipOcr.basicAccurate(get_file_content(filePath), options)
            # print(result)
            for i in result['words_result']:
                f.write('\n' + i['words'] + '\n')
os.startfile('C:/Users/win/Desktop/Pic2txt.txt')  # 自动打开生成的 txt 文件
print(i['words'])

"""

# 函数版，可自动创建文本文件

APP_ID = '27777886'
API_KEY = '4VYr2B9k5rvvOCVHYpzVaQsg'
SECRET_KEY = 'IFaIhSkWXUqq8iElNNfg9Pi1KATYfiCT'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_txt(in_path, out_path):
    for root, dirs, files in os.walk(in_path, topdown=False):
        for name in files:
            if 'jpg' in name:
                filePath = os.path.join(root, name)
                options = {
                    'detect_direction': 'true',
                    'language_type': 'CHN_ENG',
                }
                with open(out_path, 'a') as f:
                    result = aipOcr.basicAccurate(
                        get_file_content(filePath), options)
                    # print(result)
                    for i in result['words_result']:
                        f.write('\n' + i['words'] + '\n')
    os.startfile(out_path)  # 自动打开生成的 txt 文件
    # print(i['words'])


if __name__ == '__main__':

    in_path = r"D:\1jieya\image"
    out_path = r'C:/Users/win/Desktop/2_txt.txt'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # with open(filename, "w") as f:
    get_txt(in_path, out_path)
    
"""
