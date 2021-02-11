# python 合并多个 word 文档（带图片等）


# encoding=utf-8
# 导入pywin32包
import win32com.client as win32
# 打开word软件
word = win32.gencache.EnsureDispatch('Word.Application')
# 非可视化运行
word.Visible = False

output = word.Documents.Add()  # 新建合并后空白文档

# 需要合并的文档路径，这里有个文档1.docx，2.docx，3.docx.
files = ['D://jupyter notebook//操作word//1//11//1.doc',
         'D://jupyter notebook//操作word//1//11//11.docx']
for file in files:
    output.Application.Selection.Range.InsertFile(file)  # 拼接文档

# 获取合并后文档的内容
doc = output.Range(output.Content.Start, output.Content.End)
doc.Font.Name = "黑体"  # 设置字体

output.SaveAs(r'D://jupyter notebook//操作word//1//11//result.docx')  # 保存
output.Close()
