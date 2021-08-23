from aip import AipOcr
import os

# 人工智能大法好，使用百度 api 批量识别图片上的文字：
# 这是是批量识别，统统放进一个文件夹就 OK 啦～

APP_ID = '24608598'
API_KEY = 'kAHxRGWszGl95maX0GgIKpGC'
SECRET_KEY = 'NA1or974XAPSCgo7SlmMoYBzzZKhgoGM'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


for root, dirs, files in os.walk(r"D:\1jieya\remove", topdown=False):
    for name in files:
        if 'png' in name:
            filePath = os.path.join(root, name)
            options = {
                'detect_direction': 'true',
                'language_type': 'CHN_ENG',
            }
            with open('C:/Users/win/Desktop/Pic2txt.txt', 'a') as f:
                result = aipOcr.webImage(get_file_content(filePath), options)
                # print(result)
                for i in result['words_result']:
                    f.write('\n' + i['words'] + '\n')
    os.startfile(r'C:/Users/win/Desktop/Pic2txt.txt')  # 自动打开生成的 txt 文件
    # print(i['words'])
