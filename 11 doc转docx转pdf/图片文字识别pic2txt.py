import easyocr

reader = easyocr.Reader(['ch_sim', 'en'])
result = reader.readtext('D:\\11.png')
# print(result)
for i in result:
    word = i[1]
    print(word)
