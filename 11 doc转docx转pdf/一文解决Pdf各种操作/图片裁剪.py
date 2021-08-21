import os
from PIL import Image, ImageFilter, ImageDraw

# im = Image.open(r"C:\Users\win\Desktop\ccc\20200706130733539.png")

# 获取图片的格式，大小，以及模式
# print(im.format, im.size, im.mode)

# 指定图片的像素
# im.thumbnail((720, 1280))
# im.save(r"C:\Users\win\Desktop\ccc\128_128.jpg")

# 旋转图片的方向
# dest_im = im.rotate(90)
# dest_im.save(r"C:\Users\win\Desktop\ccc\90.png")

# 给图片添加滤镜
# dest_im = im.filter(ImageFilter.GaussianBlur)
# dest_im.show()

# # 图片反转
# dest_im = im.transpose(Image.FLIP_LEFT_RIGHT)
# dest_im = im.transpose(Image.FLIP_TOP_BOTTOM)
# dest_im.show()

# 图片上写文字
# image = Image.open(r"C:\Users\win\Desktop\ccc\20200706130733539.png")
# img_draw = ImageDraw.Draw(image)
# img_draw.text((1270, 1250), 'hello world!', fill='green')
# image.show()

# 批量将图片的大小设置为指定大小

in_path = r"C:\Users\win\Desktop\ccc"
out_path = os.path.join(in_path, 'modify')
if not os.path.exists(out_path):
    os.makedirs(out_path)


def modify():
    for image_name in os.listdir(in_path):
        cur_dir = in_path + '/' + image_name
        if os.path.isfile(cur_dir):
            print(f'正在处理:{cur_dir}')
            im = Image.open(cur_dir)
            im.thumbnail((1280, 720))
            im.save(os.path.join(out_path, image_name))


if __name__ == '__main__':
    modify()
