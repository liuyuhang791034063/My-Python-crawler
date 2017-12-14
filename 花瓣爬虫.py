#coding:utf-8
"""

Created at 2017年12月13日
@author : BiGbAi

"""

from urllib import request
import urllib
import re
from selenium import webdriver
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作

url = 'http://huaban.com/explore/miantiao/'
heads = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
         }

x = 1
list = []
def urlHandle(url):
    req = requests.get(url=url, params=heads)
    req.encoding = 'utf-8'
    page_pin_re = re.compile('app.page\["pins"\](.+?);', re.S)
    pins= page_pin_re.findall(req.text)[0]
    groups_select = re.compile('"pin_id":(\d+).+?"key":"(.+?)".+?', re.S)
    groups = re.findall(groups_select, pins)
    return groups

def img_dowland(groups, x):
    if groups:
        for i in groups:
            pin_id = i[0]
            pin_url = 'http://img.hb.aicdn.com/'+ i[1] + '_fw236'

            if pin_id in list:
                continue
            else:
                list.append(pin_id)
                urllib.request.urlretrieve(pin_url, 'D:\picture\%s.jpg' % x)
                x +=1
    return x

x = 1
groups = urlHandle(url)
x = img_dowland(groups, x)

while (groups):
    pin_id = groups[-1][0]
    urltemp = url + '/?max=' + str(pin_id) + '&limit=' + str(20) + '&wfl=1'
    groups = urlHandle(urltemp)
    x = img_dowland(groups, x)


