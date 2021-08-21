import os
import time
# 读取图片


def GetFile(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 从剪贴板保存图像


def GetPhoto():
    from PIL import Image, ImageGrab
    im = ImageGrab.grabclipboard()
    if isinstance(im, Image.Image) == True:
        os.mkdir(r"D:\TempPhoto")
        open(r"D:\TempPhoto\1.jpg", "w+")
        im.save(r"D:\TempPhoto\1.jpg")
        return 0
    else:
        return 1

# 调用baidu接口识别


def Identify():
    import pyperclip
    from aip import AipOcr

    # 插入你申请的密钥
    APP_ID = '24608598'
    API_KEY = 'kAHxRGWszGl95maX0GgIKpGC'
    SECRET_KEY = 'NA1or974XAPSCgo7SlmMoYBzzZKhgoGM'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = GetFile(r"D:\TempPhoto\1.jpg")
    Result = client.basicAccurate(image)
    print("查询ID：%r" % Result.get("log_id"))
    print("***************************")
    Content = Result['words_result']
    for i in range(Result.get("words_result_num")):
        print(Content[i]["words"])
    print("***************************")

    data = open(r"D:\TempPhoto\1.txt", 'a+')
    for i in range(Result.get("words_result_num")):
        print(Content[i]["words"], file=data)
    data.close()

    data = open(r"D:\TempPhoto\1.txt", "r")
    Str = data.read()
    pyperclip.copy(Str)
    data.close()
    print("Done！已复制到剪贴板")

# 清理残余文件


def Clean():
    os.remove(r"D:\TempPhoto\1.txt")
    os.remove(r"D:\TempPhoto\1.jpg")
    os.rmdir(r"D:\TempPhoto")


print("本程序可以自动识别剪贴板中的图片上的文字\n调用XXOCR接口完成功能\n识别出的文字可以直接进行复制粘贴")
print("每次尝试识别时间间隔为两秒,程序已开始运行")
t = 1
while True:
    i = GetPhoto()
    if i == 0:
        os.system("cls")
        print("发现剪贴板中的图片！")
        print("开始识别，第%d次" % t)
        Identify()
        Clean()
        t = t+1
    else:
        time.sleep(2)
