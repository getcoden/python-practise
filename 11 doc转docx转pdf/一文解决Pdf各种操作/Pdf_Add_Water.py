import os
from copy import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

if __name__ == '__main__':
    dirpath = r"D:\filep"
    filename = "科目"
    filepath = os.path.join(dirpath, filename+'.pdf')
    """添加水印"""
    watermark_filepath = os.path.join(dirpath, 'watermark.pdf')
    save_filepath = os.path.join(dirpath, filename+'【带水印】.pdf')
    """读取PDF水印文件"""
    # 可以先生成一个空白A4大小的png图片，通过 https://mp.weixin.qq.com/s/_oJA6lbsdMlRRsBf6DPxsg 教程的方式给图片加水印，将图片插入到word中并最终生成一个水印PDF文档
    watermark = PdfFileReader(watermark_filepath)
    watermark_page = watermark.getPage(0)

    pdf_reader = PdfFileReader(filepath)
    pdf_writer = PdfFileWriter()

    for page_index in range(pdf_reader.getNumPages()):
        current_page = pdf_reader.getPage(page_index)
        # 封面页不添加水印
        if page_index == 0:
            new_page = current_page
        else:
            new_page = copy(watermark_page)
            new_page.mergePage(current_page)
        pdf_writer.addPage(new_page)
    # 保存水印后的文件
    with open(save_filepath, "wb") as out:
        pdf_writer.write(out)
