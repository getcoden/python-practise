from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='ch')
img_path = r"C:\Users\win\Desktop\3.png"

result = ocr.ocr(img_path)

for line in result:
    for i in line:

        print(i[0])
