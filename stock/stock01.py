import time
import urllib.parse
import urllib.request
import json
import queue

""" 八一钢铁 """

url='https://wechatapp.futu5.com/stock/basic-quote'

# 初始化queue
q = queue.Queue(120)

values = {
    'stock_ids': '51170241965125',
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

    # 获取当前时间
    current_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    # 计算当前价格
    current_price_str = ' --当前：' + str(price / 1000)

    # 计算百分比
    current_percent_str = ' --百分比：' + str(round(((price - lastclose_price) / lastclose_price) * 100, 2)) + '%'

    # 计算1分钟变化率
    # q.put(price / 1000)
    # current_rate_str = ' --1分钟变化率：'
    # if(q.qsize() <= 1):
    #     current_rate_str += str(0)
    # else:
    #     current_rate_str += str(round((price / q.get()) / (60), 4))

    print(current_time_str + current_price_str + current_percent_str)
    time.sleep(0.5)

