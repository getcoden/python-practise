
from aip import AipOcr  # 导入AipOcr模块，用于做文字识别
import os
import time


# 函数版，可自动创建文本文件

APP_ID = '27777886'
API_KEY = '4VYr2B9k5rvvOCVHYpzVaQsg'
SECRET_KEY = 'IFaIhSkWXUqq8iElNNfg9Pi1KATYfiCT'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 如果接口 api 不能用了，看看 baidu-aip 网页免费赠送的使用额度是否用完


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def get_txt(in_path, out_path):

    path_list = os.listdir(in_path)
    path_list.sort(key=lambda x: int(x.replace("images_", "").split('.')[0]))
    # path_list.sort(key=lambda x: int(x.split('.')[0]))
    print('图片文件为:' + str(path_list) + '\n')
    print('正在上传图片进行文字识别输出......')
    for filename in path_list:
        if 'png' in filename:
            filePath = os.path.join(in_path, filename)
            options = {
                'detect_direction': 'true',
                'language_type': 'CHN_ENG',
            }
            with open(out_path, 'a') as f:
                result = aipOcr.basicAccurate(
                    get_file_content(filePath), options)
                # print(result)
                time.sleep(2)   #由于并发限制为 2 秒，在进行非纯文本认识时只能加延时2秒处理才能成功。
                for i in result['words_result']:
                    # print(i)
                    f.write('\n' + i['words'] + '\n')
    print('Done!')
    os.startfile(out_path)  # 自动打开生成的 txt 文件


if __name__ == '__main__':

    in_path = r"C:\Users\win\Desktop\11\三上第七单元试卷及练习\（彩）2"
    out_path = r'C:/Users/win/Desktop/20_txt.txt'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # with open(filename, "w") as f:
    get_txt(in_path, out_path)
