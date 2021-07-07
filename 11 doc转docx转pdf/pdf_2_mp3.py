
import pdfplumber
import pyttsx3
# 读取PDF文档
pdf = pdfplumber.open(r"D:\天翼云盘下载\《Python编程快速上手-让繁琐工作自动化》.pdf")

# 获取页数
print("总页数：", len(pdf.pages))
print("-----------------------------------------")

# 读取第4页
first_page = pdf.pages[3]
print("本页：", first_page.page_number+1)
print("-----------------------------------------")

# 导出第4页文本
text = first_page.extract_text()
print(text)
engine = pyttsx3.init()

# 去掉文本中的换行符
text = text.replace('\n', '')

# 朗读文本
engine.say(text)
engine.runAndWait()
