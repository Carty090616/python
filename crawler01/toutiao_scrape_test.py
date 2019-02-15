"""今日头条"""
"""存在问题，怀疑是多线程的问题"""

import requests
import os
import time

from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool

def get_page(offset):
    params = {
        'aid': 24,
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        print("连接错误")
        return None

def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image': image.get('url'),
                    'title': title
                }

def save_image(item):
    print('保存图片')
    if not os.path.exists('e://pic//' + item.get('title')):
        print('创建')
        os.mkdir('e://pic//' + item.get('title'))
    try:
        response = requests.get(item.get('image'))
        # time.sleep(5)
        # if requests.status_codes == 200:
        file_path = '{0}/{1}.{2}'.format('e://pic//' + item.get('title'), md5(response.content).hexdigest(), 'jpg')
        print(file_path)
        if not os.path.exists(file_path):
            with open(file_path, 'wb') as f:
                f.write(response.content)
        else:
            print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print("Fail Connection")

def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool = Pool()
    pool.map(main, groups)
    pool.close()
    pool.join()