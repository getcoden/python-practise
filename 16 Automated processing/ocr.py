# 导入easyocr
import easyocr
# 创建reader对象
reader = easyocr.Reader(['ch_sim', 'en'])
# 读取图像
result = reader.readtext('test.png')
# 结果
result
