from win32com import client as wc
from glob import glob
import os


class DocToDocx:

    def __init__(self, file_name):
        """
        因为glob函数接收的是r'D:/Note/*'，所以全部file_name添加/*
        :param file_name: 含doc文件路径
        """
        if file_name[-1] != '*' or file_name[-1] != '/':
            file_name = file_name + '/*'
        elif file_name[-1] != '*':
            file_name = file_name + '*'
        if not os.path.exists(file_name[:-2]):
            raise Exception(f'{file_name}路径不存在')
        self.file_name = file_name

    def _get_paths(self):
        if self.file_name is None:
            raise Exception(print('没有定义self.file_name'))
        return glob(self.file_name)

    def turn(self):
        paths = self._get_paths()
        w = wc.Dispatch('Word.Application')     # 打开word进程
        for path in paths:
            print(path)
            doc = w.Documents.Open(path)    # 打开doc文件
            doc.SaveAs(path+'x', 12)        # 保存为docx，12才是docx，16是doc
            # doc.Close()                   # 别关闭，关闭了报错，原因未知
        w.Quit()    # 关闭word进程


if __name__ == '__main__':
    # D:\Note,该目录文件下存储doc文件
    d = DocToDocx(r'D:\my_code\Secret_contract')
    d.turn()  # 开始转换
