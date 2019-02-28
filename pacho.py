import urllib.request
import urllib.parse
import json
import random
import time
import hashlib
#response = urllib.request.urlopen('http://pic1.win4000.com/wallpaper/2017-12-22/5a3ccec09e8ed.jpg')
#image = response.read()
#with open("fengjing.jpg",'wb') as f:
#    f.write(image)
content = input('请输入翻译内容:')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
u = 'fanyideskweb'
d = content
f = str(int(time.time()*1000) + random.randint(1,10))
c = 'sr_3(QOHT)L2dx#uuGR@r'
sign = hashlib.md5((u + d + f + c).encode('utf-8')).hexdigest()
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = f
data['sign'] = sign
data['doctype'] = 'json'
data['version'] =  '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_REALTIME'
data['typoResult'] = 'true'
#head = {}
#head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
print(type(html))
target = json.loads(html)
print(type(target))
print("翻译结果: %s"%(target["translateResult"][0][0]['tgt']))