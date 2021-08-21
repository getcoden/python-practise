import pdfplumber
import pandas as pd

path = r"D:\filep\d1.pdf"
pdf = pdfplumber.open(path)
i = 1
# writer=pd.ExcelWriter('output.xlsx')
# df = []
# df = pd.DataFrame(columns=['语文', '数据不', '右', '顺',
#    '中成药', '三国杀', '口', '中', '交', '顺'])
sheetname = ['考古文博', '历史学', '马克思主义理论', '民族学与文化学', '文学-外国文学', '文学-中国文学', '艺术学', '语言学', '哲学', '宗教学', '法学', '管理学', '环境科学', '教育学', '经济学-财政科学', '经济学-工业经济', '经济学-金融', '经济学-经济管理',
             '经济学-经济综合', '经济学-贸易经济', '经济学-农业经济', '经济学-世界经济', '人文地理学', '社会学', '体育学', '统计学', '图书馆情报与档案学', '心理学', '新闻学与传播学', '政治学-国际政治', '政治学-中国政治', '综合-高校综合性学报', '综合-综合性人文社科期刊']

# 由于存在一个表格跨页的情况，先将所有表格存放在一个DataFrame中，再根据序号拆分。
df2 = []
columns1 = ['语文', '数据不', '右', '顺',
            '中成药', '三国杀', '口', '中', '交', '顺']
# df3 = pd.DataFrame()
for page in pdf.pages[0: 2]:
    # print(page)
    # 获取当前页面的全部文本信息，包括表格中的文字
    # print(page.extract_text())
    for table in page.extract_tables():
        # print(table)
        df1 = pd.DataFrame(table[1:], columns=columns1)
        df2.append(df1)
        df3 = pd.concat(df2)
print(len(df3))
# df3.to_excel(r"D:\filep\pic.xlsx", index=False)
