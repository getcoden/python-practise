# 可以使用
from win32com.client import Dispatch
import os
from time import sleep

wdFormatPDF = 17


def doc2pdf(input_file, output_file):
    print(input_file)
    print(output_file)
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(output_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == "__main__":

    dir_word = r'D:\jupyter notebook\操作word\1\11'  # word目录
    dir_pdf = r'D:\jupyter notebook\操作word\1\11'  # pdf存放目录

    for root, dirs, filenames in os.walk(dir_word):
        for file in filenames:

            if file.endswith(".doc"):
                doc2pdf(str(dir_word + "\\" + file),
                        str(dir_pdf + "\\" + file.replace(".doc", ".pdf")))
            elif file.endswith(".docx"):
                doc2pdf(str(dir_word + "\\" + file),
                        str(dir_pdf + "\\" + file.replace(".docx", ".pdf")))

# 			sleep(1)	# 每次间隔1s
