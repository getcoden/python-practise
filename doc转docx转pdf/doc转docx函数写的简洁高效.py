from win32com import client as wc  # 导入模块


def doc_to_docx(file):
    word = wc.Dispatch("Word.Application")  # 打开word应用程序
    doc = word.Documents.Open(file)  # 打开word文件
    doc.SaveAs("{}x".format(file), 12)  # 另存为后缀为".docx"的文件，其中参数12指docx文件
    doc.Close()  # 关闭原来word文件
    word.Quit()
    print("完成！")
    return "{}x".format(file)


if __name__ == '__main__':
    # 记得。doc 文件是绝对路径地址，不然可能报错。如果想提取 word 数据，可以搜索我的另一篇博客。
    file = r"D:\my_code\Secret_contract"

    doc_to_docx(file)
