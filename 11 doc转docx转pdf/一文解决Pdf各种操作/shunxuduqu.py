import os
import cv2


def read_finger_directory(directory_name):
    imglist = os.listdir(directory_name)
    array_of_img = []  # this if for store all of the image data
    # print(imglist)
    imglist.sort(key=lambda x: int(x.replace("finger", "").split('.')[0]))
    # print("list_order:", imglist)
    # this loop is for read each image in this foder,directory_name is the foder name with images.
    for filename in imglist:
        # print(filename) #just for test
        # img is used to store the image data
        # img = cv2.imread(directory_name + "/" + filename)  #原程序目的
        img = directory_name + "/" + filename
        # print(filename)
        array_of_img.append(img)
        # print(img)
        # print(array_of_img)
    return array_of_img


result = read_finger_directory(r"D:\1\image")
print(result)

'''
path = r"D:\1\image"
path_list = os.listdir(path)
path_list.sort(key=lambda x: int(x.replace("finger", "").split('.')[0]))
# path_list.sort(key=lambda x: int(x.split('.')[0]))
print(path_list)
for filename in path_list:
    f = open(os.path.join(path, filename), 'rb')
    print(f)
'''
