# encoding:utf-8
# FileName: add_water
# Author:   xiaoyi | 小一
# email:    1010490079@qq.com
# Date:     2020/12/10 14:59
# Description:

from PIL import Image, ImageFont, ImageDraw, ImageEnhance, ImageChops
import math
import os
import random
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)


# 设置水印字体
TTF_FONT = 'font/pangmenzhengdao.ttf'
TTF_FONT = os.path.join(os.path.dirname(os.path.abspath(__file__)), TTF_FONT)


def add_mark(filepath_input, filepath_output, mark_quality):
    """
    添加水印，然后保存图片
    @param filepath_input:
    @param filepath_output:
    @param mark_quality:
    @return:
    """
    im = Image.open(filepath_input)
    image = mark(im)
    name = os.path.basename(filepath_input)

    if image:
        if not os.path.exists(filepath_output):
            os.mkdir(filepath_output)

        new_name = os.path.join(filepath_output, name)
        if os.path.splitext(new_name)[1] != '.png':
            image = image.convert('RGB')
        image.save(new_name, quality=mark_quality)
        print(name + " Success.")
    else:
        print(name + " Failed.")


def set_opacity(im, opacity):
    """
    设置水印透明度
    @param im:
    @param opacity:
    @return:
    """
    assert opacity >= 0 and opacity <= 1

    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)

    return im


def crop_image(im):
    """
    裁剪图片边缘空白
    @param im:
    @return:
    """
    bg = Image.new(mode='RGBA', size=im.size)
    diff = ImageChops.difference(im, bg)
    del bg
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im


def get_mark_style(im, mark, style='random'):
    """
    设置水印位置
    @param im:
    @param mark:
    @param style:
    @return:
    """
    # 居上水印
    x_0 = int(im.size[0] / 2 - mark.size[0] / 2)
    y_0 = int(0 + mark.size[1] * 0.75)
    # 居中水印
    x_1 = int(im.size[0] / 2 - mark.size[0] / 2)
    y_1 = int(im.size[1] / 2)
    # 底部居中
    x_2 = int(im.size[0] / 2 - mark.size[0] / 2)
    y_2 = int(im.size[1] - mark.size[1]*1.5)
    # 底部靠左
    x_3 = int(0 + mark.size[0] * 0.2)
    y_3 = int(im.size[1] - mark.size[1]*1.5)
    # 底部靠右
    x_4 = int(im.size[0] - mark.size[0] * 1.2)
    y_4 = int(im.size[1] - mark.size[1]*1.5)

    mark_list = [[x_0, y_0], [x_1, y_1], [x_2, y_2], [x_3, y_3], [x_4, y_4]]
    if style == 'random':
        # 默认随机位置水印
        mark_style = random.choice(mark_list)
    elif style == 'top':
        mark_style = [x_0, y_0]
    elif style == 'center':
        mark_style = [x_1, y_1]
    elif style == 'bottom_center':
        mark_style = [x_2, y_2]
    elif style == 'bottom_left':
        mark_style = [x_3, y_3]
    elif style == 'bottom_right':
        mark_style = [x_4, y_4]
    else:
        mark_style = random.choice(mark_list)

    x = mark_style[0]
    y = mark_style[1]

    return x, y


def gen_mark(mark_content='公众号【小一的学习笔记】', mark_color='#232862', mark_space=75, mark_angle=30,
             mark_size=50, mark_opacity=0.05, mark_type='location', location='random'):
    """
    生成mark图片，返回添加水印的函数
    @param mark_content:
    @param mark_color:
    @param mark_space:
    @param mark_angle:
    @param mark_size:
    @param mark_opacity:
    @param mark_type:
    @param bottom_right:
    @return:
    """
    # 字体宽度
    width = len(mark_content) * mark_size
    # 创建水印图片(宽度、高度)
    mark = Image.new(mode='RGBA', size=(width, mark_size))
    # 生成文字
    draw_table = ImageDraw.Draw(im=mark)
    draw_table.text(xy=(0, 0), text=mark_content, fill=mark_color,
                    font=ImageFont.truetype(TTF_FONT, size=mark_size)
                    )

    draw_table.text(xy=(0, 0), text=mark_content, fill=mark_color,
                    font=ImageFont.truetype(TTF_FONT, size=mark_size))
    del draw_table
    # 裁剪空白
    mark = crop_image(mark)
    # 透明度
    set_opacity(mark, mark_opacity)

    def mark_im_location(im):
        """
        在特定位置创建水印
        @param im:
        @return:
        """
        # 创建一模一样的原图并添加水印
        mark2 = Image.new(mode='RGBA', size=(im.size[0], im.size[1]))
        x, y = get_mark_style(im, mark, location)
        mark2.paste(mark, (x, y))

        # 在原图上添加大图水印
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        im.paste(mark2, (0, 0), mask=mark2.split()[3])

        del mark2

        return im

    def mark_im_full(im):
        """
        在im图片上添加水印 im为打开的原图
        @param im:
        @return:
        """
        # 计算斜边长度
        c = int(math.sqrt(im.size[0]*im.size[0] + im.size[1]*im.size[1]))
        """创建满屏的水印"""
        # 以斜边长度为宽高创建大图（旋转后大图才足以覆盖原图）
        mark2 = Image.new(mode='RGBA', size=(c, c))
        # 在大图上生成水印文字，此处mark为上面生成的水印图片
        y, idx = 0, 0
        while y < c:
            # 制造x坐标错位
            x = -int((mark.size[0] + mark_space)*0.5*idx)
            idx = (idx + 1) % 2

            while x < c:
                # 在该位置粘贴mark水印图片
                mark2.paste(mark, (x, y))
                x = x + mark.size[0] + mark_space
            y = y + mark.size[1] + mark_space

        # 将大图旋转一定角度
        mark2 = mark2.rotate(mark_angle)

        # 在原图上添加大图水印
        if im.mode != 'RGBA':
            im = im.convert('RGBA')
        im.paste(
            mark2, (int((im.size[0]-c)/2), int((im.size[1]-c)/2)),  mask=mark2.split()[3])

        del mark2

        return im

    if mark_type == "full":
        return mark_im_full
    else:
        return mark_im_location


if __name__ == '__main__':
    """设置参数"""
    dirpath_input = r"D:\The main thing\11个顶级Github存储库\craw_project-master\pic_tools\pic_bg"            # 图像路径
    filepath_output = 'D:/filep/'            # 输出水印图像的文件夹，如果没有则在当前目录下主动创建
    mark_content = '小一的学习笔记'      # 水印内容，默认是 "小一的学习笔记"。可不设置
    mark_color = '#232862'              # 水印颜色，默认是 #232862【灰色】。可不设置
    mark_space = 75                     # 水印之间的空隙，默认值为 75。可不设置
    mark_angle = 30                     # 水印的角度，默认是 30°。可不设置
    mark_size = 35                      # 水印字体的大小，默认是 50。
    mark_opacity = 0.15                 # 水印透明度，默认是 0.05，数值越小越透明。可不设置
    mark_quality = 90                   # 图片输出质量，默认是。可不设置

    """水印设置"""
    for filename in os.listdir(dirpath_input):
        print(filename + " processing...")
        filepath_input = os.path.join(dirpath_input, filename)
        # 生成水印
        mark = gen_mark(mark_content, mark_color, mark_space, mark_angle, mark_size, mark_opacity,
                        mark_type='full',
                        # mark_type='location',   # 水印填充方式：全屏 full 、特定位置 location
                        # 水印位置：random、top、center、bottom_center、bottom_left、bottom_right。默认center居中
                        location='bottom_center'
                        )
        # 添加水印
        add_mark(filepath_input, filepath_output, mark_quality)
