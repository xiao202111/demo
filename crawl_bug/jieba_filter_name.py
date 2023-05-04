import re

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    start = 123976467
    url = f'https://m.138txt.net/206/206582/{start}_{1}.html'  # 要拉取的网页 URL
    index = 1
    for i in range(2, 1000):
        response = requests.get(url)  # 获取返回对象
        # 解析 HTML
        if response.status_code == 200:  # 连接状态成功时，将 HTML 文本转换为 BeautifulSoup 对象
            soup = BeautifulSoup(response.text, 'html.parser')  # 待解析的HTML或XML文档，内置解释器
            # print(soup)
            # 使用 BeautifulSoup 对象查询 HTML 中的元素和属性
            title = soup.title.string
            links = soup.find_all('div', attrs={'id': 'nr1'})
            if len(links) == 0:
                start = start + index
                index = 1
                url = f'https://m.138txt.net/206/206582/{start}_{index}.html'  # 要拉取的网页 URL
                continue
            # 打印解析结果
            text = re.sub(r"\s+", "\n", links[0].text)
            with open('LJXZ.txt', 'a', encoding='utf-8') as f:
                f.write(text)
            print(url)
            index = index + 1
            url = f'https://m.138txt.net/206/206582/{start}_{index}.html'  # 要拉取的网页 URL
        else:
            start = start + index
            index = 1
            url = f'https://m.138txt.net/206/206582/{start}_{index}.html'  # 要拉取的网页 URL
    else:
        # 处理错误
        print(f'Request failed with status code {response.status_code}')