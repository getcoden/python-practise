import os
import re
import fitz


def extract_pic_info(filepath, pic_dirpath):
    """
    提取PDF中的图片
    @param filepath:pdf文件路径
    @param pic_dirpath:要保存的图片目录路径
    @return:
    """
    if not os.path.exists(pic_dirpath):
        os.makedirs(pic_dirpath)
    # 使用正则表达式来查找图片
    check_XObject = r"/Type(?= */XObject)"
    check_Image = r"/Subtype(?= */Image)"
    img_count = 0

    """1. 打开pdf，打印相关信息"""
    pdf_info = fitz.open(filepath)
    # 1.16.8版本用法 xref_len = doc._getXrefLength()
    # 最新版本
    xref_len = pdf_info.xref_length()
    # 打印PDF的信息
    print("文件名：{}, 页数: {}, 对象: {}".format(filepath, len(pdf_info), xref_len-1))

    """2. 遍历PDF中的对象，遇到是图像才进行下一步，不然就continue"""
    for index in range(1, xref_len):
        # 1.16.8版本用法 text = doc._getXrefString(index)
        # 最新版本
        text = pdf_info.xref_object(index)

        is_XObject = re.search(check_XObject, text)
        is_Image = re.search(check_Image, text)
        # 如果不是对象也不是图片，则不操作
        if is_XObject or is_Image:
            img_count += 1
            # 根据索引生成图像
            pix = fitz.Pixmap(pdf_info, index)
            pic_filepath = os.path.join(
                pic_dirpath, 'img_' + str(img_count) + '.png')
            """pix.size 可以反映像素多少，简单的色素块该值较低，可以通过设置一个阈值过滤。以阈值 10000 为例过滤"""
            # if pix.size < 10000:
            #     continue

            """三、 将图像存为png格式"""
            if pix.n >= 5:
                # 先转换CMYK
                pix = fitz.Pixmap(fitz.csRGB, pix)
            # 存为PNG
            pix.writePNG(pic_filepath)


# 提取图片内容
filepath = r"D:\科目.pdf"
pic_dirpath ='D:/'

extract_pic_info(filepath, pic_dirpath)
