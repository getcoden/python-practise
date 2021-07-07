from docx import Document
from docx.shared import RGBColor, Pt, Cm
import os
import glob

out_path = r"C:\Users\win\Desktop\result"
if not os.path.exists(out_path):
    os.mkdir(out_path)

Keyword = '校园欺凌'
file_path = r"C:\Users\win\Desktop\xx"

for file in glob.glob(file_path + '\*.docx'):
    docx = Document(file)
    for paragraph in docx.paragraphs:
        for run in paragraph.runs:
            if Keyword in run.text:
                run.font.bold = True
                run.font.color.rgb = RGBColor(255, 0, 0)
    docx.save(out_path + '/' + os.path.basename(file))
