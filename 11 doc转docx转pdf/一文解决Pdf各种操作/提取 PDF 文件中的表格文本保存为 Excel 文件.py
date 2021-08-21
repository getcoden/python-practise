import pdfplumber
from openpyxl import Workbook


def extract_table(pdf_file):
    wb = Workbook()
    wb.remove(wb.worksheets[0])
    with pdfplumber.open(pdf_file) as pdf:
        index = 0
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                ws = wb.create_sheet(title=f'Sheet{index}')
                for row in table:
                    ws.append(row)
                index = index+1
    wb.save(r'D:\filep\提取结果.xlsx')


extract_table(r"D:\filep\d1.pdf")
