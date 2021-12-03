# -*- coding: utf-8 -*-
# @Author: ander
# @Date:   2021-07-29 18:22:18
# @Last Modified by:   ander
# @Last Modified time: 2021-08-11 16:54:22
import time
from datetime import datetime
from tempfile import TemporaryDirectory
import yagmail
import pandas as pd
import requests
from django.core.cache import cache
from bs4 import BeautifulSoup
import json

def task1(name):
    print("Hello!")
    time.sleep(3)
    print(name)


def send_email(data):
    print(data)
    with TemporaryDirectory() as tmp_folder:
        cache_data = cache.get(data['sid'])
        orders_df = pd.read_json(cache_data, orient='table')
        dt = datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
        file_path = f'{tmp_folder}/{dt}.csv'
        orders_df.to_csv(file_path, encoding='gbk')

        yag = yagmail.SMTP(user='2429260713@qq.com', password='amhjcvlmupncebae', host='smtp.qq.com')
        content = ['订单数据表格请见附件。', file_path]
        yag.send(data['email'], data['subject'], content)

    return True


def zhihu_spider():
    url = 'https://www.zhihu.com/topic/19553176/hot'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    result = []
    data = json.loads(soup.select_one('#js-initialData').string.strip())
    for k, v in data['initialState']['entities']['answers'].items():
        result.append({
            'author': v['author']['name'],
            'content': v['excerpt']
        })
    cache.set('spider-zhihu', result, None)
    return  True
