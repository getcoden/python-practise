# 安装fitz需要安装PyMuPDF才能使用
import fitz
import os


def pdf_to_jpg(name):

    pdfdoc = fitz.open(name)
    temp = 0
#     print(dir(fitz.Matrix))
    for pg in range(pdfdoc.page_count):
        page = pdfdoc[pg]
        temp += 1
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高四倍的图像。
        zoom_x = 1.33333333
        zoom_y = 1.33333333
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
#         print(dir(page))
        pm = page.get_pixmap(matrix=trans, alpha=False)

        pic_name = '{}.jpg'.format(temp)
        # 拼接生成pdf的文件路径
        pic_pwd = os.path.join('', pic_name)
        print(pic_name)
#         print(dir(pm._writeIMG))
        pm._writeIMG(pic_pwd, 1)


pdf_to_jpg(r"D:\天翼云盘下载\电子工业版l六年级上册信息技术教案(安徽版)(第七册)教案 - 百度文库.pdf")
