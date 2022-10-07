from aip import AipOcr
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


def get_txt(in_path, out_path):
    for root, dirs, files in os.walk(in_path, topdown=False):
        for name in files:
            if 'png' in name:
                filePath = os.path.join(root, name)
                options = {
                    'detect_direction': 'true',
                    'language_type': 'CHN_ENG',
                }
                with open(out_path, 'a') as f:
                    result = aipOcr.webImage(
                        get_file_content(filePath), options)
                    # print(result)
                    for i in result['words_result']:
                        f.write('\n' + i['words'] + '\n')
    os.startfile(out_path)  # 自动打开生成的 txt 文件
    # print(i['words'])


if __name__ == '__main__':

    in_path = r"D:\1jieya\remove"
    out_path = r'C:/Users/win/Desktop/Pic_2_txt.txt'
    get_txt(in_path, out_path)
