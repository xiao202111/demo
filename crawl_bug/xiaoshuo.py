import json
import time

import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import pickle
from selenium import webdriver


if __name__ == '__main__':
    # 获取执行文件所在的目录
    dirname = os.path.dirname(os.path.abspath(__file__))
    # 将当前工作目录更改为执行文件所在的目录
    os.chdir(dirname)

    driver = webdriver.Chrome('./chromedriver')

    df = pd.read_excel('./daikuan_correct.xlsx')
    df = df.iloc[:, :18]

    for i in range(53, 54):
        # 每类处理
        df_list = df.iloc[i].tolist()
        non_empty_standard_name = [x for x in df_list if pd.notna(x)]

        url = f'https://www.mee.gov.cn/searchnew/?searchword={non_empty_standard_name[0]}'  # 要拉取的网页 URL
        response = driver.get(url)  # 获取返回对象,html形式
        html = driver.page_source
        print(html)
        time.sleep(100)

        # # 保存 Response 对象到文件中
        # with open('response.pickle', 'wb') as f:
        #     pickle.dump(response, f)
        # # print(response)

        # for search_name in non_empty_standard_name:
        #         url = f'https://www.mee.gov.cn/searchnew/?searchword={search_name}.html'  # 要拉取的网页 URL
        #         response = requests.get(url).content.decode()  # 获取返回对象
        #         print(response)
        #         # 解析 HTML
        #         if response.status_code == 200:  # 连接状态成功时，将 HTML 文本转换为 BeautifulSoup 对象
        #             soup = BeautifulSoup(response.text, 'html.parser')  # 待解析的HTML或XML文档，内置解释器