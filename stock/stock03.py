import time
import urllib.parse
import urllib.request
import json

""" 财通证券 """

url='https://wechatapp.futu5.com/stock/basic-quote'
values = {
    'stock_ids': '74878461439572',
    'market_type': '3',
    'data_type': '0',
    'uid': '-1',
    '_': '1552981875300'
}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data.encode('utf-8'))
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

while(True):
    response = urllib.request.urlopen(req)

    # 转换为json
    json_data=json.loads(response.read())
    # print(json_data)

    lastclose_price = int(json_data.get('data').get('stock_quote_items')[0].get('lastclose_price'))
    price = int(json_data.get('data').get('stock_quote_items')[0].get('price'))

    print('当前：' + str(price / 1000) + '--百分比：' + str(round(((price - lastclose_price) / lastclose_price) * 100, 2)) + '%')
    time.sleep(0.5)


