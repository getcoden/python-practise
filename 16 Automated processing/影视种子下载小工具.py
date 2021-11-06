import requests
import re
from urllib.parse import quote
from bs4 import BeautifulSoup
from pathlib import Path
import os

os.chdir(r"F:\My_Code")
class GetBt:
    def __init__(self):
        self.keyword = ''
        self.page_num = 1
        self.movie_name = []
        self.movie_url = []
        self.url = 'https://www.btbtt11.com/search-index-keyword-' + \
            quote(self.keyword) + '.htm'

    def get_data(self):
        self.url = 'https://www.btbtt11.com/search-index-keyword-' + quote(
            self.keyword) + '-page-' + str(self.page_num) + '.htm'
        respone = requests.get(url=self.url)
        return respone.text

    def get_title(self):
        data = BeautifulSoup(self.get_data(), 'lxml')
        try:
            result = data.find(attrs={'class': 'body threadlist'}).find_all(
                attrs={'target': '_blank'})
            for i in range(len(result)):
                infilt_result = str(result[i].get('title')).find('BT下载')
                if infilt_result != -1:
                    self.movie_name.append(
                        str(result[i].get('title')).replace('<span class=red>', '').replace('</span>', ''))
                    self.movie_url.append(str(result[i].get('href')))
            try:
                page = data.find(attrs={'class': 'page'}).text
                if page.find('下一页') != -1:
                    return True
                else:
                    return False
            except AttributeError:
                return False
        except AttributeError:
            print('无资源')
            return None

    def get_all_page(self):
        self.keyword = input('请输入你需要查询的资源名：')
        state = self.get_title()
        if state is not None:
            while state is True and self.page_num < 10:  # 最大10页面
                self.page_num += 1
                state = self.get_title()
            else:
                pass
            for n in range(len(self.movie_name)):
                print(str(n + 1) + '. ' + self.movie_name[n])
            print(str(len(self.movie_name) + 1) + '. ' + '没有我想要的资源')
            return True
        else:
            return None

    def down_bt(self):
        state = self.get_all_page()
        if state is not None:
            num = input('请输入要下载的序号:')
            if int(num) < len(self.movie_name) + 1:
                url = 'https://www.btbtt11.com/' + self.movie_url[int(num) - 1]
                name = self.movie_name[int(num) - 1].replace('/', '_')
                re.sub("[\\/:*?\"<>|]", ' ', name)
                file = Path(os.getcwd() + '/' + name)
                if file.is_dir():
                    pass
                else:
                    os.mkdir(name)
                respone = requests.get(url)
                soup = BeautifulSoup(respone.text, 'lxml')
                bt_page_url = soup.find(attrs={'class': 'attachlist'}).find_all(
                    attrs={'rel': 'nofollow'})
                for i in range(len(bt_page_url)):
                    bt_name = bt_page_url[i].text
                    bt_herf = bt_page_url[i].get('href')
                    bt_down_url = 'https://www.btbtt11.com/' + \
                        bt_herf.replace('dialog', 'download')
                    down = requests.get(bt_down_url, stream=True)
                    print('正在下载 ' + bt_name)
                    with open(name + '/' + bt_name, "wb") as code:
                        code.write(down.content)
                print('所有下载完成')
            else:
                pass


if __name__ == '__main__':
    while True:
        GetBt().down_bt()
