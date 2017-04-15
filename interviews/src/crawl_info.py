import urllib
from urllib.parse import quote
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver

# my_text = '深圳市腾讯计算机系统有限公司'
#
# url = 'http://www.tianyancha.com/search?key=%s' % quote(my_text)
# print(url)
# result = urllib.request.urlopen(url).read().decode('utf-8')  # 搜索结果页的内容
# soup = BeautifulSoup(result)
# print(soup)

url = 'http://www.tianyancha.com/search'
my_text = '深圳市腾讯计算机系统有限公司'

browser = webdriver.Firefox()
browser.get(url)
browser.find_element_by_id('live-search').send_keys(my_text)
browser.find_element_by_class_name('input-group-addon input-search-new').click()
print(browser.title)
browser.quit()