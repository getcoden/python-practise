from paddleocr import PaddleOCR
import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from paddleocr import PaddleOCR, draw_ocr
font = cv2.FONT_HERSHEY_SIMPLEX

# 这个可以完整运行，用的是通用识别库模型进行识别

# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=False,
                rec_model_dir=r"D:\PaddleOcr\inference\ch_ppocr_server_v2.0_rec_infer",
                cls_model_dir=r"D:\PaddleOcr\inference\ch_ppocr_mobile_v2.0_cls_infer",
                det_model_dir=r"D:\PaddleOcr\inference\ch_ppocr_server_v2.0_det_infer")  # need to run only once to download and load model into memory


def pic2txt(dir_path):
    with open(r"C:\Users\win\Desktop\1.txt", 'a') as f:
        for file in os.listdir(dir_path):
            img_path = os.path.join(dir_path, file)
            print(img_path)
            result = ocr.ocr(img_path, cls=True)
            for line in result:
                print(line[1][0])
                f.write(line[1][0]+'\n')


path = r"D:\1jieya\remove"
pic2txt(path)
