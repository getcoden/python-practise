from pdf2docx import Converter
import re

# 传入文件绝对路径


def pdf_to_word(fileName):
    pdf_file = fileName
    # 正则获取不含文件类型后缀的部分，用于组成word文档绝对路径
    name = re.findall(r'(.*?)\.', pdf_file)[0]
    docx_file = f'{name}.docx'

    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()


fileName = r"D:\科目.pdf"
pdf_to_word(fileName)
