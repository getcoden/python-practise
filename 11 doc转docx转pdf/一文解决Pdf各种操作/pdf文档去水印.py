from itertools import product
from PIL import Image

# img = Image.open(r"D:\1jieya\image\images_0.png")
# width, height = img.size
# for pos in product(range(width), range(height)):
#     if sum(img.getpixel(pos)[:3]) > 600:
#         img.putpixel(pos, (255, 255, 255))
# img.save(r"C:\Users\win\Desktop\removed_1.png")


import os
import sys
import pandas as pd
import numpy as np
from datetime import datetime

input = r"D:\1jieya\image"
output = r"D:\1jieya\remove"


def modify():
    for image_name in os.listdir(input):
        print(image_name)
        img = Image.open(os.path.join(input, image_name))
        width, height = img.size
        for pos in product(range(width), range(height)):
            if sum(img.getpixel(pos)[:3]) > 600:
                img.putpixel(pos, (255, 255, 255))
        img.save(os.path.join(output, image_name))


if __name__ == '__main__':
    modify()
