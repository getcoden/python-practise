import fitz  # pip install PyMuPDF
import glob
import img2pdf
import os
import datetime


def from_photo_to_pdf(photo_path):
    startTime_pdf2img = datetime.datetime.now()  # 开始时间
    # 1、生成地址列表
    photo_list = os.listdir(photo_path)
    photo_list = [os.path.join(photo_path, i) for i in photo_list]

    # 1、指定pdf的单页的宽和高
    # A4纸张
    # a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    # 我的自定义：
    a4inpt = (img2pdf.mm_to_pt(720), img2pdf.mm_to_pt(1080))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    with open(photo_path+'\\1result.pdf', 'wb') as f:
        f.write(img2pdf.convert(photo_list, layout_fun=layout_fun))

    endTime_pdf2img = datetime.datetime.now()  # 结束时间
    print('img2pdf 时间=', (endTime_pdf2img - startTime_pdf2img).seconds)


# if __name__ == '__main__':
#     photo_path = r"D:\1jieya\image"
#     from_photo_to_pdf(photo_path)


def pic2pdf(img_dir):
    doc = fitz.open()
    for img in sorted(glob.glob("{}/*".format(img_dir))):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)  # 打开图片
        pdfbytes = imgdoc.convertToPDF()  # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)  # 将当前页插入文档
    if os.path.exists("allimages.pdf"):
        os.remove("allimages.pdf")
    doc.save("allimages.pdf")  # 保存pdf文件
    doc.close()


if __name__ == '__main__':
    img_dir = r"D:\1jieya\image"
    pic2pdf(img_dir)
