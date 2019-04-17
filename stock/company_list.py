import time
import urllib.parse
import urllib.request
import json
import queue
import mysql as sql

url='https://wzq.tenpay.com/cgi-bin/stockquotation.fcgi'

values = {
    'action': '3',
    'rank': '1',
    'limit': '50',
    'market': 'HS',
    'boardtype': '0',
    'qluin': 'os-ppuF2jhG56TzT1mLXvuMJ4tfU',
    'qlskey': 'v0ae789cc115c9b0666819fe57c92363',
    'scenes': '5'
}

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data.encode('utf-8'))
req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN')

response = urllib.request.urlopen(req)

# 转换为json
json_data=json.loads(str(response.read().decode('utf-8')).replace("\\x2B","").replace("\\x20",""))
print(json_data)

json_res_code = json_data.get("retcode")

if json_res_code == '0':
    json_array = json_data.get("stock")

    for out in json_array:
        print(out.get("code") + out.get("name"))
        sql.insert(out.get("code"), out.get("name"));

else:
    print(json_res_code)