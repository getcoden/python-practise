#  可以使用，但只能单个操作，后期有时间进行扩展为批量处理的功能
from win32com import client
import os
import win32com.client as wc
word = wc.gencache.EnsureDispatch('Word.Application')

# Doc另存为Docx


def saveAsDocx(file):
    word.Visible = False
    word.DisplayAlerts = False
    doc = word.Documents.Open(file, False)  # 打开文档，不提示转换确认框
    new_file = file.split('.')[0] + '.docx'
    doc.SaveAs(new_file, 12)
    doc.Close()

    return new_file


saveAsDocx(r'D:\jupyter notebook\操作word\1\11\1.doc')


# 可借鉴这个的循环写法

# python 批量将文件夹内所有 doc 转成 docx  完美运行


def doc_to_docx(path):
    if os.path.splitext(path)[1] == ".doc":
        word = client.Dispatch('Word.Application')
        doc = word.Documents.Open(path)  # 目标路径下的文件
        doc.SaveAs(os.path.splitext(path)[0]+".docx", 16)  # 转化后路径下的文件
        doc.Close()
        word.Quit()


path = r"D:\my_code\Secret_contract"  # 填写文件夹路径
doc_to_docx(path)
