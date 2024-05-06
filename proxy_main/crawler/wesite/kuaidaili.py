import re
import requests
import json
from proxy_main.crawler.base import BaseCrawler
from proxy_main.configure.config import NUMBERS,MIN_NUMBERS
url_main = 'https://www.kuaidaili.com/free/inha/{}'



class kuaidaili(BaseCrawler):
    def __init__(self) -> None:
        self.url = [url_main.format(i) for i in range(MIN_NUMBERS,NUMBERS)]
    def parse(self,html):
        pattern = re.compile('fpsList.*?(\[\{.*);')
        value = json.loads(pattern.findall(html)[0])
        for item in value:
            yield item
# k = kuaidaili()
# for data in k.crawl():
#     print(data)
#     proxy = {
#         'http': 'http://'+data.host+":"+data.port,
#         'https' : 'http://'+data.host+":"+data.port
#     }
#     try:
#         resp = requests.get('https://httpbin.org/get',proxies=proxy)
#         if resp.status_code ==200:
#             print(f'{data}连接可用')
#             with open('proxy.txt','a') as f:
#                 f.write(data.host+":"+data.port)
#                 f.write('\n')
#     except Exception as e:
#         print("此链接无法使用")