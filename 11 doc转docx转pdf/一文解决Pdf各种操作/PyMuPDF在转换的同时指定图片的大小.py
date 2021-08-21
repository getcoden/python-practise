# PDF 文档页数超过 100 页的话需要十几秒，因为先转换成一整张 1056X816 的图片，再对本地文件中的所有图片进行遍历截图，时间上比较慢，通过查看文档发现：
# 还可以在转换的同时指定图片的大小，对图片指定区域进行截取，这样快很多，一步到位，省去了二次截图的过程，前提使我们必须要知道想要截取哪一块区域并保存

'''
#下面的这段代码就是想要从一页PDF的中心点为起点截取到右下角的区域，截取整张图的1/4.
>>> mat = fitz.Matrix(2, 2)                  # 在每个方向缩放因子2
>>> rect = page.rect                         # 页面的矩形
>>> mp = rect.tl + (rect.br - rect.tl) * 0.5 # 矩形的中心
>>> clip = fitz.Rect(mp, rect.br)            # 我们想要的剪切区域
>>> pix = page.getPixmap(matrix = mat, clip = clip)
 
'''
# 实际用到的例子是：
# 整张图片导出之后是 1056*816，但是我想要的是这张图片最底部的部分 1056*75，相当于 PDF 文档的页脚部分。
import sys
import fitz
import os
import datetime


def pyMuPDF_fitz(pdfPath, imagePath):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间

    pdfDoc = fitz.open(pdfPath)
    for pg in range(pdfDoc.pageCount):
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=72
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pix = page.getPixmap(matrix=mat, alpha=False)

        if not os.path.exists(imagePath):  # 判断存放图片的文件夹是否存在
            os.makedirs(imagePath)  # 若图片文件夹不存在就创建

        pix.writePNG(imagePath+'/'+'images_%s.png' % pg)  # 将图片写入指定的文件夹内

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('pdf2img时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


def pyMuPDF2_fitz(pdfPath, imagePath):
    pdfDoc = fitz.open(pdfPath)  # open document
    for pg in range(pdfDoc.pageCount):  # iterate through the pages
        page = pdfDoc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像
        # 此处若是不做设置，默认图片大小为：792X612, dpi=72
        zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
        zoom_y = 1.33333333
        # 缩放系数1.3在每个维度  .preRotate(rotate)是执行一个旋转
        mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        rect = page.rect                         # 页面大小
        mp = rect.tl + (rect.bl - (0, 280/zoom_x))  # 矩形区域    56=75/1.3333
        clip = fitz.Rect(mp, rect.br)            # 想要截取的区域
        pix = page.getPixmap(matrix=mat, alpha=False, clip=clip)  # 将页面转换为图像
        if not os.path.exists(imagePath):
            os.makedirs(imagePath)
        pix.writePNG(imagePath+'/'+'psReport_%s.png' %
                     pg)  # store image as a PNG


if __name__ == "__main__":
    pdfPath = r"D:\1jieya\python自动化系列2.0.pdf"
    imagePath = r"D:\1jieya\image1"
    # pyMuPDF_fitz(pdfPath, imagePath)#只是转换图片
    pyMuPDF2_fitz(pdfPath, imagePath)  # 指定想要的区域转换成图片


# 当然上面这种是综合下来最快的，另外再介绍一种方法 pdf2image
