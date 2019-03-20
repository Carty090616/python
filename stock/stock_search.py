import urllib.request
import json

url='https://wechatapp.futu5.com/stock/search?keyword=FDFH&_=1552981875300'
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')

response = urllib.request.urlopen(req)

# 转换为json
json_data=json.loads(response.read())
print(json_data.get('data').get('list')[0].get('stock_id'))


