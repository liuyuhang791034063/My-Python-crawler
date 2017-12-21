#coding=utf-8
import requests
from selenium import webdriver
import time
import urllib
from PIL import Image

url = 'http://xiyou.fanya.chaoxing.com/portal'
brower = webdriver.Chrome()
brower.get(url)
time.sleep(1)
brower.maximize_window()
#获取当前窗口的句柄
old_handle = brower.current_window_handle

brower.find_element_by_class_name('zu_l_submit').click()
brower.find_element_by_class_name('zl_input').send_keys('04161086')
brower.find_element_by_class_name('zl_input2').send_keys('791034063')
yanzhengma = input()
brower.find_elements_by_class_name('zc_input32')[0].send_keys(str(yanzhengma))
brower.find_element_by_class_name('zl_btn_right').click()
brower.find_element_by_class_name('zaf_text').click()
time.sleep(3)

handles = brower.window_handles
for i in handles:
    if i == old_handle:
        continue
    else:
        brower.switch_to_window(i)
        time.sleep(3)
print(brower.page_source)