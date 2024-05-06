from proxy_main.utils.proxy import Proxy
from retrying import retry
from proxy_main.configure.config import headers_list
import requests
import random
import time

class BaseCrawler:
    @retry(stop_max_attempt_number=3, retry_on_result=lambda x: x is None, wait_fixed=2000)
    def fetch(self):
        try:
            for url in self.url:
                time.sleep(10)
                print('-------------------')
                response = requests.get(url=url,headers=random.choice(headers_list))
                if response.status_code == 200:
                    response.encoding = 'utf-8'
                    yield response.text
                else:
                    print(response.status_code)
        except Exception as e:
            print(f"网络连接出错了{e}")
    def crawl(self):
        for html in self.fetch():
            for proxy in self.parse(html):
                yield Proxy(host = proxy.get('ip'),port = proxy.get('port'))