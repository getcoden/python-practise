import os
import pdfplumber


def extract_text_info(filepath):
    """
    提取PDF中的文字
    @param filepath:文件路径
    @return:
    """
    with pdfplumber.open(filepath) as pdf:
        # 获取第2页数据
        page = pdf.pages[1]
        print(page.extract_text())


# 提取文字内容
extract_text_info(r"D:\pdf\Docker入门教程.pdf")


# 可以看到，直接通过下标即可定位到相应的页码，从而通过 extract_text 函数提取该也的所有文字
# 而如果想要提取所有页的文字，只需要改成：

with pdfplumber.open(filepath) as pdf:
 # 获取全部数据
    for page in pdf.pages
        print(page.extract_text())
