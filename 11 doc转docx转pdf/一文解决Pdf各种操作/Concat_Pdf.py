from PyPDF2 import PdfFileReader, PdfFileWriter
import os
'''
比起拆分来，合并的思路更加简单：
确定要合并的 文件顺序
循环追加到一个文件块中
保存成一个新的文件
对应的代码比较简单：
'''


def concat_pdf(filename, read_dirpath, save_filepath):
    """
    合并多个PDF文件
    @param filename:文件名
    @param read_dirpath:要合并的PDF目录
    @param save_filepath:合并后的PDF文件路径
    @return:
    """
    pdf_writer = PdfFileWriter()
    # 对文件名进行排序
    list_filename = os.listdir(read_dirpath)
    list_filename.sort(key=lambda x: int(x[:-4].replace(filename, "")))
    for filename in list_filename:
        print(filename)
        filepath = os.path.join(read_dirpath, filename)
        # 读取文件并获取文件的页数
        pdf_reader = PdfFileReader(filepath)
        pages = pdf_reader.getNumPages()
        # 逐页添加
        for page in range(pages):
            pdf_writer.addPage(pdf_reader.getPage(page))
    # 保存合并后的文件
    with open(save_filepath, "wb") as out:
        pdf_writer.write(out)
    print("文件已成功合并，保存路径为："+save_filepath)


filename = 'Docker入门教程'
read_dirpath = r"D:\2.0\co"
save_filepath = r'D:\2.0\Docker入门教程.pdf'

concat_pdf(filename, read_dirpath, save_filepath)
