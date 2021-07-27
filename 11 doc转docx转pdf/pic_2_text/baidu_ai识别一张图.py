from aip import AipOcr

# 新建一个AipOcr对象  识别不全文字
config = {
    'appId': '24608598',
    'apiKey': 'kAHxRGWszGl95maX0GgIKpGC',
    'secretKey': 'NA1or974XAPSCgo7SlmMoYBzzZKhgoGM'
}
client = AipOcr(**config)


# 识别图片里的文字
def img_to_str(image_path):
    # 读取图片
    with open(image_path, 'rb') as fp:
        image = fp.read()

        # 调用通用文字识别, 图片参数为本地图片
    result = client.basicGeneral(image)
    # 返回拼接结果
    if 'words_result' in result:
        for w in result['words_result']:
            print(w['words'])
        # return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__':
    print(img_to_str(r"D:\11\9.jpg"))
