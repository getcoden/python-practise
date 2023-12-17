
'''
import os
from PyPDF2 import PdfFileWriter, PdfFileReader


def split_pdf(filename, filepath, save_dirpath, step=5):
    """
    拆分PDF为多个小的PDF文件，
    @param filename:文件名
    @param filepath:文件路径
    @param save_dirpath:保存小的PDF的文件路径
    @param step: 每step间隔的页面生成一个文件，例如step=5，表示0-4页、5-9页...为一个文件
    @return:
    """
    if not os.path.exists(save_dirpath):
        os.mkdir(save_dirpath)
    pdf_reader = PdfFileReader(filepath)
    # 读取每一页的数据
    pages = pdf_reader.getNumPages()
    for page in range(0, pages, step):
        pdf_writer = PdfFileWriter()
        # 拆分pdf，每 step 页的拆分为一个文件
        for index in range(page, page+step):
            if index < pages:
                pdf_writer.addPage(pdf_reader.getPage(index))
        # 保存拆分后的小文件
        save_path = os.path.join(
            save_dirpath, filename+str(int(page/step)+1)+'.pdf')
        print(save_path)
        with open(save_path, "wb") as out:
            pdf_writer.write(out)

    print("文件已成功拆分，保存路径为："+save_dirpath)


filename = 'Docker入门教程.pdf'
filepath = r"D:\pdf\Docker入门教程.pdf"
save_dirpath = r"D:\2.0"
split_pdf(filename, filepath, save_dirpath, step=5)
'''

import fitz
import os


def convert_pdf2img(file_relative_path):
    """
    file_relative_path : 文件相对路径
    """
    page_num = 1
    filename = file_relative_path.split('.')[-2]
    if not os.path.exists(filename):
        os.makedirs(filename)
    pdf = fitz.open(file_relative_path)
    for page in pdf:
        rotate = int(0)
        # 每个尺寸的缩放系数为2，这将为我们生成分辨率提高4的图像。
        # 此处若是不做设置，默认图片大小为：792X612, dpi=96
        zoom_x = 2 # (2-->1584x1224)
        zoom_y = 2
        mat = fitz.Matrix(zoom_x, zoom_y)
        pixmap = page.get_pixmap(matrix=mat, alpha=False)
        pixmap.pil_save(f"{filename}/{page_num}.png")
        print(f"第{page_num}保存图片完成")
        page_num = page_num + 1
if __name__ =="__main__":
    # 文件夹中文件名
    file_relative_path = r"D:\1jieya\22.pdf"
    convert_pdf2img(file_relative_path)