from win32com.client import Dispatch, constants, gencache
import time
import os
from win32com import client

path = r'D:\my_code\Secret_contract'
start_time = time.time()
files = os.listdir(path)
gencache.EnsureModule('{00020905-0000-0000-C000-000000000046}', 0, 8, 4)
wd = Dispatch('Word.Application')
for file in files:
    if file.split('.')[-1] in ['docx', 'doc']:
        word_path = path + '\\' + file
        file_list = (file.split('.')[-2::-1])[::-1]
        pdf_file = "".join(file_list)
        pdf_path = path + '\\' + pdf_file + '.pdf'
        print('正在转换：')
        print('《{}》'.format(file))
        doc = wd.Documents.Open(word_path, ReadOnly=1)
        doc.ExportAsFixedFormat(pdf_path, constants.wdExportFormatPDF, Item=constants.wdExportDocumentWithMarkup,
                                CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
        print('上述文件转换完成！')
        print('')
wd.Quit(constants.wdDoNotSaveChanges)
end_time = time.time()
print("该文件夹下的Word文件已转为PDF，用时：{:.2f}秒！".format(end_time-start_time))
time.sleep(5)
