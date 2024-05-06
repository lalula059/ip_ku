import json
import requests
from parsel  import Selector
import re
url = 'https://www.kuaidaili.com/free/inh    a/'
url1 = 'https://httpbin.org/get'
headers ={
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
}

resp = requests.get(url=url1,headers=headers)
print(resp.text)
# print(resp.text)
data_anly = Selector(resp.text)
# value = data_anly.xpath('//tr[@data-row-key="undefined"]').getall()
# pattern = re.compile('fpsList.*?(\[\{.*);')
# value = json.loads(pattern.findall(resp.text)[0])
# print(value)