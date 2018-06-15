# -*- coding: utf-8 -*-


import requests
import configparser
from bs4 import BeautifulSoup
import re
import urllib3


url = r"https://blog.csdn.net/a906423355/article/details/78272016"
headers = {
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
requests.packages.urllib3.disable_warnings()
http = urllib3.PoolManager()
r = http.request('GET', 'https://blog.csdn.net/a906423355/article/details/78272016', headers=headers)
print(r.status)
print(r.data.decode())
